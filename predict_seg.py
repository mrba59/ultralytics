from argparse import ArgumentParser

from ultralytics import YOLO
import time
import cv2
import tqdm
import numpy as np
import os

model = YOLO("/home/reda/Documents/projets/ultralytics/yolov8x-seg.pt")
model.to('cuda')
path = ['/home/reda/Documents/projets/results_yolo/tournoi3/crop/frame409/box_9.jpg',
        '/home/reda/Documents/projets/results_yolo/tournoi3/crop/frame409/box_8.jpg',
        '/home/reda/Documents/projets/results_yolo/tournoi3/crop/frame399/box_8.jpg',
        '/home/reda/Documents/projets/results_yolo/tournoi3/crop/frame474/box_8.jpg',
        '/home/reda/Documents/projets/results_yolo/tournoi3/crop/frame412/box_12.jpg',
        '/home/reda/Documents/projets/results_yolo/tournoi3/crop/frame714/box_8.jpg',
        '/home/reda/Documents/projets/results_yolo/tournoi3/crop/frame714/box_4.jpg']
crop_path = '/home/reda/Documents/projets/results_yolo/tournoi3/crop/'
list_frame = os.listdir(crop_path)
list_box_occlusion = []
for frame in list_frame:
    for box in os.listdir(os.path.join(crop_path, frame)):
        if box[-3:] == 'jpg':
            path = os.path.join(crop_path, frame, box)
            result = model.predict(path, conf=0.25)
            if len(result[0].boxes) >= 2:
                list_box_occlusion.append(path)

print(list_box_occlusion)