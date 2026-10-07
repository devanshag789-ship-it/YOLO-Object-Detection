import cv2
from ultralytics import YOLO

# Load YOLOv8 model (auto-downloads first time)
model = YOLO("yolov8n.pt")  # n = nano (fast, laptop-friendly)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("YOLO Object Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
