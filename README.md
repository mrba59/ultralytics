# YOLOv8 with ReID and Tracking

This repository is a fork of the [YOLOv8 by Ultralytics](https://github.com/ultralytics/ultralytics) with added ReID (Re-identification) model and tracking algorithm, integrated via the [TorchReID repository](https://github.com/KaiyangZhou/deep-person-reid). This enhancement allows for advanced object tracking capabilities by combining object detection with ReID.

## Table of Contents

- [Requirements and Installation](#requirements-and-installation)
- [Usage](#usage)
- [References](#references)

## Requirements

This project requires dependencies from both the YOLOv8 and TorchReID repositories, along with additional GPU hardware for optimal performance.

- **YOLOv8 by Ultralytics:** Refer to their [installation guide](https://github.com/ultralytics/ultralytics#installation) for setup details.
  
- **TorchReID:** Refer to the [TorchReID installation guide](https://github.com/KaiyangZhou/deep-person-reid#installation) for setup details.

## How to Use

To utilize the YOLOv8 model with the integrated ReID and tracking algorithm, use the `track.py` script. This script is configured using YAML configuration files that define the tracking parameters.

### Configuration

- **`track.yaml`**: Located in the root directory, this file controls the general parameters for the detetction model.

- **`botsort.yaml`**: Located in `ultralytics/cfg/trackers/botsort.yaml`, this file is specifically for configuring the BoT-SORT algorithm, which is the only tracking algorithm currently implemented.

  - **Example Parameters in `botsort.yaml`:**
    - `reid_model`: Path to the ReID model.
    - `conf_thres`: Confidence threshold for detections.
    - `iou_thres`: IOU threshold for association.

Ensure these files are properly configured before running the model.

### Running the Model

To run the YOLOv8 model with ReID and BoT-SORT tracking, use the following command:

```bash
python track.py

