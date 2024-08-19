from ultralytics import YOLO
import time
import tqdm


# model = YOLO("/home/reda/Documents/projets/ultralytics/runs/detect/yolov8_robo_human_aerial_view_person/weights/best.pt")
# model = YOLO("/home/reda/Documents/projets/ultralytics/runs/detect/yolov8_aerial_view_person_1280p2/weights/best.pt")
#model = YOLO("yolov8x.pt")
# model = YOLO("/home/reda/Documents/projets/ultralytics/runs/detect/yolov8_robo2/weights/best.pt")

# video = "/home/reda/Documents/Dataset/france_croatie_fps10.mp4"
# video = "/home/reda/Documents/drone/tournoi_warhem/DJI_0070_cut.MP4"
# video = "/home/reda/Documents/drone/usld_17_06_sept/DJI_0010.MP4"
# video = "/home/reda/Documents/drone/usld_17_06_sept/DJI_0008.MP4"


model = YOLO("/home/reda/Documents/projets/ultralytics/runs/detect/yolov8_robo/weights/best.pt")
model.to('cuda')
video = "/home/reda/Documents/tetegehm_malo.mp4"



nb_pred_list = []
start = time.time()
for result in tqdm.tqdm(
        model.track(video, conf=0.4, persist=True, tracker="botsort.yaml", save=True, stream=True, save_txt=True,
                    batch=16, save_conf=True, show_labels=True, boxes=True, show_conf=True, vid_stride=2, iou=0.7,
                    project="/home/reda/Documents/projets/results_yolo/", name="tournoi_yolov8x")):
    nb_pred_list.append(len(result.boxes))

