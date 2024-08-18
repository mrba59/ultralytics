import os.path
from argparse import ArgumentParser

from ultralytics import YOLO
import time
import cv2
import tqdm
import numpy as np


def write_yolo_labels(output_path, boxes):
    with open(output_path, 'w') as f:
        for box in boxes:
            line = map(str, box)
            line = ' '.join(line)
            f.write(line + "\n")
        f.close()


model = YOLO("/home/reda/Documents/ultralytics/runs/segment/yolov8_field_seg/weights/best.pt")
data = "/home/reda/Documents/drone/rosen_esquelbeck_10_09/DJI_0022.MP4"
model.to('cuda')
i = 0
output_path= "/home/reda/Documents/results_yolo/rosendael_esquel_19/field/labels_bbox/"
if not os.path.isdir((output_path)):
    os.mkdir(output_path)
num_frame = 1
for result in tqdm.tqdm(model.predict(data, stream=True, save_txt=True, batch=8,
                                      project="/home/reda/Documents/results_yolo/rosendael_esquel_19/", name="field")):
    list_boxes = result.boxes.data.tolist()
    for l in list_boxes:
        l.insert(0, int(float(l[-1])))
        l.pop(-1)
    write_yolo_labels(os.path.join(output_path, "DJI_0022_"+str(num_frame)+".txt"), list_boxes)
    num_frame+=1
