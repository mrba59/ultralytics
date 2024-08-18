from ultralytics import YOLO
model = YOLO('/home/reda/Téléchargements/yolov8l-face.pt')
model.predict(data, conf=conf, iou=iou, save=save, stream=stream, save_txt=save_txt, batch=8,
              save_conf=save_conf, project=output_path, name=output_name)):