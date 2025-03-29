import cv2
import os
import json
from datetime import datetime
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def run_detection_once():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        return {"error": "Unable to capture frame"}

    results = model(frame)

    detection_info = None

    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls_id = int(box.cls[0].item())
            conf = float(box.conf[0].item())
            label = model.names[cls_id]

            if label == "person" and conf > 0.5:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename = f"person_{timestamp}.jpg"
                path = os.path.join("app", "detections", filename)
                frame = r.plot()
                cv2.imwrite(path, frame)

                detection_info = {
                    "label": label,
                    "confidence": round(conf, 2),
                    "timestamp": timestamp,
                    "image": filename
                }

                # Log to detections.json
                log_path = os.path.join("app", "detections.json")
                with open(log_path, "r+") as f:
                    data = json.load(f)
                    data.append(detection_info)
                    f.seek(0)
                    json.dump(data, f, indent=4)

                break

    return detection_info or {"message": "No person detected"}
