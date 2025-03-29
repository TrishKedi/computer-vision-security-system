import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.detections import router as detection_router

app = FastAPI()

app.include_router(detection_router, prefix='/api', tags=['detections'])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow requests from React
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

os.makedirs("app/detections", exist_ok=True)

if not os.path.exists("app/detections.json"):
    with open("app/detections.json" ,'w') as file:
        file.write("[]")

@app.get("/")
def root():
    return {"message": "AI Smart Security detection"}
