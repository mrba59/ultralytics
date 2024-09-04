# YOLOv8 with ReID and Tracking

This repository is a fork of the [YOLOv8 by Ultralytics](https://github.com/ultralytics/ultralytics) with added ReID (Re-identification) model and tracking algorithm, integrated via the [TorchReID repository](https://github.com/KaiyangZhou/deep-person-reid). This enhancement allows for advanced object tracking capabilities by combining object detection with ReID.

## Table of Contents

- [Requirements and Installation](#requirements-and-installation)
- [Usage](#usage)
- [References](#references)

## Requirements and Installation

This project requires dependencies from both the YOLOv8 and TorchReID repositories, along with additional GPU hardware for optimal performance.

- **YOLOv8 by Ultralytics:** Refer to their [installation guide](https://github.com/ultralytics/ultralytics#installation) for setup details.
  
- **TorchReID:** Refer to the [TorchReID installation guide](https://github.com/KaiyangZhou/deep-person-reid#installation) for setup details.

## How to Use

To run YOLOv8 model with the integrated ReID and tracking algorithm, use the `track.py` script. This script is configured using YAML configuration files that define the tracking and detector parameters.

### Configuration

- **`track.yaml`**: Located in the root directory, this file controls the general parameters for tracking.

- **`botsort.yaml`**: Located in `ultralytics/cfg/trackers/botsort.yaml`, this file is specifically for configuring the BoT-SORT algorithm, which is the only tracking algorithm currently implemented.

  - **Example Parameters in `botsort.yaml`:**
    - `reid_checkpoint_path:`: Path to your ReID model.
    - `field`: This parameter is used to filter detected objects within a specified area of the frame. If your camera is stationary and you want to restrict detection to a particular region of interest, you can specify the coordinates of this area using this parameter else set to None. 

      - **Usage**: 
        - If you want to focus detection on a specific region, you can pass the coordinates of the area (e.g., boundaries or a polygon). This is useful for applications where you know that objects of interest are only present within a defined area.
        - If your video footage is not constrained to a fixed area or you do not wish to restrict detection to a specific region, set this parameter to `none`. This will ensure that the detection algorithm evaluates the entire frame.

Ensure these files are properly configured before running the model.

### Running the Model

To run the YOLOv8 model with ReID and BoT-SORT tracking, use the following command, 


```bash
python track.py

