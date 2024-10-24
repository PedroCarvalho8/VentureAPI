import cv2
import json
import os
from ultralytics import YOLO
from collections import defaultdict
from src.repositories.db_interaction import *

def detection():
    model = YOLO('src/models/Challenge_SPI.pt')
    model_classes = model.names
    print(model_classes)
    model.predict(source=0, show=False, conf=0.7, verbose=False, stream=True)
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

            results = model(frame)

            for result in results:
                for box in result.boxes:
                    class_name = result.names[int(box.cls)]
                    object_counts[class_name] += 1
                    total_objects_detected += 1

                    if itens_solicitados:
                        idxs_to_remove = []

                        detected_class_name = str(class_name).upper()
                        class_list = [json.loads(i[1]).get('class_name').upper() for i in itens_solicitados]

                        if detected_class_name in class_list:
                            idx_to_remove = [i for i, c in enumerate(class_list) if c == detected_class_name]
                            idxs_to_remove.extend(idx_to_remove)

                        idxs_to_remove = [idx for idx in idxs_to_remove if idx < len(itens_solicitados)]

                        if itens_solicitados and idxs_to_remove:
                            for idx in sorted(set(idxs_to_remove), reverse=True):
                                if 0 <= idx < len(itens_solicitados):
                                    item_encontrado(json.loads(itens_solicitados[idx][1]).get('class_name'))
                                    send_msg(
                                        json.dumps({
                                            'class_name': json.loads(itens_solicitados[idx][1]).get('class_name').upper(),
                                            'object_count': object_counts[class_name],
                                        }),
                                        table='detected_items'
                                    )
                                    itens_solicitados.pop(idx)

                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                    cv2.putText(frame, f'{class_name} {object_counts[class_name]}',
                                (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

            cv2.imshow("YOLOv8 Detection", frame)

            frame_path = f"temp_frames/frame_{frame_idx}.jpg"
            cv2.imwrite(frame_path, frame)

            frame_idx += 1

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    detection()
