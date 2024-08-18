import argparse
from argparse import ArgumentParser
from ultralytics import YOLO
import time
import tqdm
import numpy as np


def main(args):
    print(f"Model Path: {args.model_path}")
    print(f"Video Path: {args.video_path}")
    print(f"IOU Threshold: {args.iou}")
    print(f"Confidence Threshold: {args.conf}")
    print(f"Output Path: {args.output_path}")
    print(f"Output Name: {args.output_name}")
    print(f"Stream: {args.stream}")
    print(f"Save TXT: {args.save_txt}")
    print(f"Save Confidence: {args.save_conf}")
    print(f"vid_stride: {args.vid_stride}")

    nb_pred_list = []
    model = YOLO(args.model_path)
    model.to('cuda')
    start = time.time()
    for result in tqdm.tqdm(
            model.predict(args.video_path, conf=args.conf, iou=args.iou, save=True, stream=args.stream, save_crop=args.save_crop, save_txt=args.save_txt,
                          batch=8,
                          save_conf=args.save_conf, project=args.output_path, name=args.output_name, vid_stride=1)):
        nb_pred_list.append(len(result.boxes))
        pass
    print(f"elapsed time  {time.time() - start}")
    print(f" mean nb of object inside image: {np.mean(np.array(nb_pred_list))}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process video with YOLOv8")

    parser.add_argument("model_path", type=str, help="Path to the model file (e.g., best.pt)")
    parser.add_argument("video_path", type=str, help="Path to the video file (e.g., DJI_0070_cut.MP4)")

    parser.add_argument("--iou", type=float, default=0.5, help="IOU threshold for NMS (default: 0.5)")
    parser.add_argument("--conf", type=float, default=0.25, help="Confidence threshold for detection (default: 0.25)")

    parser.add_argument("--output_path", type=str, default="./",
                        help="Path to save the output files (default: current directory)")
    parser.add_argument("--output_name", type=str, default="output", help="Name for the output files (default: output)")

    parser.add_argument("--stream", action="store_true", help="Stream the video while processing")
    parser.add_argument("--save_txt", action="store_true", help="Save the detection results to a TXT file")
    parser.add_argument("--save_conf", action="store_true", help="Save the confidence scores in the output")
    parser.add_argument("--vid_stride", type=int, help="Take every x frames from a video")
    parser.add_argument("--save_crop", action="store_true", help="Save as crop object detected")

    args = parser.parse_args()
    main(args)

"""results = model(args.video_path, conf=args.conf, save=True, stream=args.stream, save_txt=args.save_txt,
                   save_conf=args.save_conf, show_labels=True, show_boxes=True, show_conf=True,
                   vid_stride=args.vid_stride, iou=args.iou,
                   project=args.output_path, name=args.output_name)"""

# model = YOLO("/home/reda/Documents/ultralytics/runs/segment/yolov8x_seg/weights/best.pt")
# model = YOLO("/home/reda/Documents/ultralytics/runs/detect/yolov8n_custom/weights/best.pt")
# model = YOLO("/home/reda/Documents/ultralytics/runs/detect/yolov8_robo_human/weights/best.pt")
# model = YOLO("rosen.pt")
# model = YOLO("/home/reda/Documents/ultralytics/runs/detect/yolov8_robo2/weights/best.pt")

# from ndarray
# im2 = cv2.imread("/home/reda/Documents/Tracking/results/images_det/frame_6000.jpg")
# video = "/home/reda/Documents/Dataset/france_croatie_fps10.mp4"
# video = "/home/reda/Documents/drone/usld_lefrin_27_sept/DJI_0039.MP4"
# video = "/home/reda/Documents/drone/usld_17_06_sept/DJI_0010.MP4"
# video = "/home/reda/Documents/drone/usld_17_06_sept/DJI_0008.MP4"
# dir_ = "/home/reda/Documents/Dataset/france_croatie_cut"

