import time
import cv2
import json
import os
from ultralytics import YOLO
from collections import defaultdict
from src.repositories.db_interaction import *
from src.repositories.arduino_interaction import movimentacao, Movimentacao


def draw_text_with_background(image, text, pos, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=0.7, font_color=(255, 255, 255),
                              font_thickness=2, bg_color=(0, 0, 0), padding=5):
    """Função para desenhar texto com fundo para melhor legibilidade."""
    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_w, text_h = text_size

    x, y = pos
    x_bg = x - padding
    y_bg = y - text_h - padding
    w_bg = text_w + 2 * padding
    h_bg = text_h + 2 * padding

    cv2.rectangle(image, (x_bg, y_bg), (x_bg + w_bg, y_bg + h_bg), bg_color, -1)

    cv2.putText(image, text, (x, y), font, font_scale, font_color, font_thickness)


def detection():
    model = YOLO('src/models/Challenge_SPI.pt')
    model_classes = model.names
    print(model_classes)
    model.predict(source=0, show=False, conf=0.8, verbose=False, stream=True)
    cap = cv2.VideoCapture(0)
    object_counts = defaultdict(int)
    total_objects_detected = 0

    if not os.path.exists("temp_frames"):
        os.makedirs("temp_frames")

    itens_solicitados = []

    try:
        frame_idx = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Falha ao capturar o vídeo.")
                break

            itens_recebidos = get_msg(table='items_to_detect')

            if itens_recebidos:
                for i in itens_recebidos:
                    itens_solicitados.append(i)

            idxs_to_remove = []

            for idx, item in enumerate(itens_solicitados[:]):

                item_status = False

                start_time = time.time()

                movimentacao.andar(Movimentacao.Direcoes.FRENTE)

                while not item_status:

                    results = model(frame)

                    for result in results:

                        if not item_status:

                            for box in result.boxes:

                                if not item_status:

                                    class_name = result.names[int(box.cls)]
                                    object_counts[class_name] += 1
                                    total_objects_detected += 1

                                    if itens_solicitados:
                                        detected_class_name = str(class_name).upper()
                                        class_name_requested = json.loads(item[1]).get('class_name').upper()

                                        if detected_class_name == class_name_requested:
                                            idxs_to_remove.append(idx)
                                            item_status = True

                                        idxs_to_remove = [idx for idx in idxs_to_remove if idx < len(itens_solicitados)]

                                        if itens_solicitados and idxs_to_remove and item_status:
                                            item_encontrado(json.loads(json.loads(item[1]).get('class_name')))
                                            send_msg(
                                                json.dumps({
                                                    'class_name': json.loads(item[1]).get('class_name').upper(),
                                                    'object_count': object_counts[class_name],
                                                }),
                                                table='detected_items'
                                            )

                                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                                    draw_text_with_background(frame, f'{class_name} {object_counts[class_name]}',
                                                              (x1, y1 - 10), font_scale=0.7, font_thickness=2,
                                                              bg_color=(50, 50, 50), font_color=(255, 255, 255))

                        frame[0:60, 0:200] = (0, 0, 0)

                        draw_text_with_background(frame, f'Status: {movimentacao.status.value}', (10, 20),
                                                  font_scale=0.6, font_thickness=2, bg_color=(0, 0, 0),
                                                  font_color=(255, 255, 255))
                        draw_text_with_background(frame, f'Frame: {frame_idx}', (10, 50),
                                                  font_scale=0.6, font_thickness=2, bg_color=(0, 0, 0),
                                                  font_color=(255, 255, 255))

                        draw_text_with_background(frame, f'Total detectado: {total_objects_detected}', (10, 80),
                                                  font_scale=0.6, font_thickness=2, bg_color=(0, 0, 0),
                                                  font_color=(255, 255, 255))

                        cv2.imshow("YOLOv8 Detection", frame)

                        frame_path = f"temp_frames/frame_{frame_idx}.jpg"
                        cv2.imwrite(frame_path, frame)

                        frame_idx += 1

                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break

                end_time = time.time()
                elapsed_time = end_time - start_time

                movimentacao.andar(Movimentacao.Direcoes.TRAS)
                time.sleep(elapsed_time)

                movimentacao.parar()

            for idx in sorted(set(idxs_to_remove), reverse=True):
                if 0 <= idx < len(itens_solicitados):
                    itens_solicitados.pop(idx)

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    detection()
