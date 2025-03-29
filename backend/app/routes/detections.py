import os
import json
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.services.capture import capture_footage
from app.utils import run_detection_once

DETECTIONS_DIR = 'detections'
os.makedirs(DETECTIONS_DIR, exist_ok=True)

router = APIRouter()

@router.get('/detections')
def get_detections():
 
    # check path exists
    if not os.path.exists("app/detections.json"):
        raise HTTPException(status_code=404, detail="File not found")
    
    with open('app/detections.json', 'r') as file:

        return json.load(file)
    
@router.get('/image/{file_name}')
def get_image(file_name: str):

    file_path = os.path.join("app", DETECTIONS_DIR, file_name)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="The file does not exist")

    return FileResponse(file_path)
    
@router.post('/detect')
def trigger_detection():
    try:
        return run_detection_once()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to trigger detection")
