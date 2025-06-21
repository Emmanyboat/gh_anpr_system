from PIL import Image
from ultralytics import YOLO

model = YOLO("best.pt")  # Your trained model

def detect_plate(img):
    result = model(img)[0]
    for r in result.boxes.data:
        x1, y1, x2, y2, conf, cls = r
        plate = result.names[int(cls)]
        return plate  # or return full result
    return None
