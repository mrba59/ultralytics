import argparse
from ultralytics import YOLO
import time
import tqdm


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
    model = YOLO(args.model_path)
    results = model(args.video_path, conf=args.conf, save=True, stream=args.stream, save_txt=args.save_txt,
                   save_conf=args.save_conf, show_labels=True, show_boxes=True, show_conf=True,
                   vid_stride=args.vid_stride, iou=args.iou,
                   project=args.output_path, name=args.output_name)
    for result in results:
        boxes = result.boxes  # Boxes object for bounding box outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs
        obb = result.obb  # Oriented boxes object for OBB outputs
        # result.show()  # display to screen
        # result.save(filename="result.jpg")  # save to disk
    # Your processing logic goes here


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

    args = parser.parse_args()
    main(args)
