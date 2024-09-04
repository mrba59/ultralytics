from ultralytics import YOLO

# Load the model.
model = YOLO("/home/reda/Documents/ultralytics/runs/detect/yolov8_robo_human/weights/best.pt")

# Training.
results = model.train(
    data='/home/reda/Documents/Dataset/aerial_view_person_v2/data.yaml',
    imgsz=960,
    epochs=100,
    batch=12,
    pretrained=True,
    name='yolov8_robo_human_aerial_view_person')
