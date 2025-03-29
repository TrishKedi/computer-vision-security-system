import cv2
import os
import json
from datetime import datetime
from ultralytics import YOLO


def capture_footage():
    # Create folders if not present
    os.makedirs("app/detections", exist_ok=True)
    if not os.path.exists("app/detections.json"):
        with open("app/detections.json", "w") as f:
            json.dump([], f)

    # Load YOLOv8 model
    model = YOLO("yolov8n.pt")  # You can also try yolov8s.pt for better accuracy

    # Start webcam
    cap = cv2.VideoCapture(0)

    print("[INFO] Starting detection... Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)

        # Extract detections
        for r in results:
            boxes = r.boxes
            for box in boxes:
                cls_id = int(box.cls[0].item())
                conf = float(box.conf[0].item())
                label = model.names[cls_id]

                if label == "person" and conf > 0.5:
                    # Draw bounding box
                    frame = r.plot()

                    # Save frame
                    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    filename = f"person_{timestamp}.jpg"
                    filepath = f"app/detections/person_{timestamp}.jpg"
                    cv2.imwrite(filepath, frame)

                    # Log detection
                    detection = {
                        "label": label,
                        "confidence": round(conf, 2),
                        "timestamp": timestamp,
                        "image": filename
                    }
                    with open("app/detections.json", "r+") as f:
                        data = json.load(f)
                        data.append(detection)
                        f.seek(0)
                        json.dump(data, f, indent=4)

                    print(f"[DETECTED] Person at {timestamp} | Saved {filename}")

        # Show feed
        cv2.imshow("Security Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_footage()


