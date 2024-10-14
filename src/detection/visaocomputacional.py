import cv2
import json
from ultralytics import YOLO
from collections import defaultdict

from src.repositories.db_interaction import send_msg


def detection():
    model = YOLO('src/models/best.pt')
    model.predict(source=0, show=False, conf=0.4, verbose=False, stream=True)

    object_counts = defaultdict(int)

    cap = cv2.VideoCapture(0)

    total_objects_detected = 0

    while True:

        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)

        for result in results:
            for box in result.boxes:
                class_name = result.names[int(box.cls)]
                object_counts[class_name] += 1
                total_objects_detected += 1

                send_msg(
                    json.dumps({
                        'class_name': class_name,
                        'object_count': object_counts[class_name]
                    }),
                    table='detected_items'
                )

        cv2.imshow("YOLOv8 Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detection()
