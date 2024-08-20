import os

import yaml
from ultralytics import YOLO
import time
import tqdm
import numpy as np


def main(config):
    print(f"Model Path: {config['model_path']}")
    print(f"Video Path: {config['video_path']}")
    print(f"IOU Threshold: {config['iou']}")
    print(f"Confidence Threshold: {config['conf']}")
    print(f"Output Path: {config['output_path']}")
    print(f"Output Name: {config['output_name']}")
    print(f"Stream: {config['stream']}")
    print(f"Save TXT: {config['save_txt']}")
    print(f"Save Confidence: {config['save_conf']}")
    print(f"vid_stride: {config['vid_stride']}")

    nb_pred_list = []
    model = YOLO(config['model_path'])
    model.to('cuda')
    start = time.time()
    for result in tqdm.tqdm(
            model.predict(config['video_path'],
                          conf=config['conf'],
                          iou=config['iou'],
                          save=config['save'],
                          stream=config['stream'],
                          save_crop=config['save_crop'],
                          save_txt=config['save_txt'],
                          batch=8,
                          save_conf=config['save_conf'],
                          project=config['output_path'],
                          name=config['output_name'],
                          vid_stride=config['vid_stride'])):
        nb_pred_list.append(len(result.boxes))
        pass
    print(f"elapsed time  {time.time() - start}")
    print(f" mean nb of object inside image: {np.mean(np.array(nb_pred_list))}")


if __name__ == "__main__":
    # Load the YAML configuration
    with open('predict.yaml', 'r') as file:
        config = yaml.safe_load(file)

    # Run the main function with the loaded config
    main(config)
    config_save_path = os.path.join(config['output_path'], ['output_name'], 'predict.yaml')
    with open(config_save_path, 'w') as file:
        yaml.dump(config, file)

    print(f"Configuration file saved to: {config_save_path}")
