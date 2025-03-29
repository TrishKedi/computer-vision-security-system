# 🔐 AI-Powered Computer Vision Security System

A real-time, edge-ready security system that uses AI and Computer Vision to detect people through a camera feed, log detections, and expose a full-stack dashboard to monitor and manage events. Built using the latest technologies: YOLOv8, FastAPI, Next.js, Docker, and OpenCV.

![demo]()

---

## 🚀 Tech Stack

| Layer        | Tech                                     |
|--------------|------------------------------------------|
| 👁️ CV Engine | YOLOv8, OpenCV                           |
| 🧠 Backend   | FastAPI (Python), Uvicorn                |
| 💻 Frontend  | Next.js (React), Tailwind CSS            |
| 📦 DevOps    | Docker, Docker Compose (optional)        |
| 💡 Edge-Ready| Jetson Nano or TensorFlow Lite (future)  |

---

## ✅ Features

- Real-time person detection using YOLOv8
- Automatically saves detection frames with timestamp
- Logs detection metadata (confidence, time, image)
- FastAPI backend with REST API:
  - `GET /detections` - list detections
  - `GET /image/:filename` - fetch saved images
  - `POST /detect` - trigger detection from API
- Next.js dashboard to view all detections
- Fully modular and ready for Edge AI deployment

---

## 📸 Demo

> _Add a GIF or video demo here showing: detection, saved logs, and dashboard interface._

---

## 🧑‍💻 Local Development Setup

### 1. Clone the repo

```bash
git clone https://github.com/TrishKedi/ai-security-system.git
cd ai-security-system
