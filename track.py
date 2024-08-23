import os
import json
import yaml
from ultralytics import YOLO
import time
import tqdm
import numpy as np
import pickle

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
    print(f"tracker: {config['tracker']}")

    nb_pred_list = []
    model = YOLO(config['model_path'])
    model.to('cuda')
    start = time.time()
    for result in tqdm.tqdm(
            model.track(config['video_path'],
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
                        vid_stride=config['vid_stride'],
                        tracker=config['tracker'],
                        classes=config['classes'])):
        nb_pred_list.append(len(result.boxes))
        pass

    print(f"elapsed time  {time.time() - start}")
    print(f" mean nb of object inside image: {np.mean(np.array(nb_pred_list))}")
    return model


if __name__ == "__main__":
    # Load the YAML configuration
    with open('track.yaml', 'r') as file:
        config = yaml.safe_load(file)

    # Run the main function with the loaded config
    model = main(config)
    dirs = [d for d in os.listdir(config['output_path']) if
            d.startswith(config['output_name'])]
    latest_dir = max(dirs, key=lambda d: os.path.getctime(os.path.join(config['output_path'], d)))
    config_save_path = os.path.join(config['output_path'], latest_dir, 'track.yaml')
    with open(config_save_path, 'w') as file:
        yaml.dump(config, file)

    with open(os.path.join('ultralytics/cfg/trackers/', config['tracker']), 'r') as file:
        config_tracker_type = yaml.safe_load(file)
    config_tracker_type_path = os.path.join(config['output_path'], latest_dir, config['tracker'])
    with open(config_tracker_type_path, 'w') as file:
        yaml.dump(config_tracker_type, file)

    print(f"Configuration file saved to: {config_save_path}")

    lost_tracker = model.predictor.trackers[0].lost_stracks
    tracker_path = os.path.join(config['output_path'], latest_dir, 'tracker_dict.json')
    lost_tracker_dict = {}
    for track in lost_tracker:
        lost_tracker_dict['features'] = track.curr_feat.tolist()
        lost_tracker_dict['start_frame'] = track.start_frame
        lost_tracker_dict['end_frame'] = track.end_frame
        lost_tracker_dict['tracklet_len'] = track.tracklet_len
        lost_tracker_dict['track_id'] = track.track_id
        lost_tracker_dict['xywh'] = track.xywh.tolist()

    with open(tracker_path, 'w') as file:
        json.dump(lost_tracker_dict, file, indent=4)
    print(f"tracker object saved in: {tracker_path}")

"""nb_pred_list = []
start = time.time()
for result in tqdm.tqdm(
        model.track(video, conf=0.4, persist=True, tracker="botsort.yaml", save=True, stream=True, save_txt=True,
                    batch=16, save_conf=True, show_labels=True, boxes=True, show_conf=True, vid_stride=2, iou=0.7,
                    project="/home/reda/Documents/projets/results_yolo/", name="tournoi_yolov8x")):
    nb_pred_list.append(len(result.boxes))"""
