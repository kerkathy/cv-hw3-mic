# cv-hw3-mic
Task 1: object detection on source dataset

Task 2: unsupervised domain adaptation on target dataset

## MIC (for Task 2)
Forked from [lhoyer/MIC](https://github.com/lhoyer/MIC).

### Environment
Please follow the instruction in [INSTALL.md](MIC/det/INSTALL.md) to install and use this repo.
For installation problems, please consult issues in [maskrcnn-benchmark](https://github.com/facebookresearch/maskrcnn-benchmark).

### Inference
```
./hw3_inference.sh /path/to/dataset /path/to/output.json <checkpoint_num>
# e.g., ./hw3_inference.sh ../hw3/data/hw3_dataset output_test.json 1 
```
`checkpoint_num` can be 0 to 4.
* 0: checkpoint trained for 0 epochs
* 1: checkpoint trained for 24000 epochs
* 2: checkpoint trained for 42000 epochs
* 3: checkpoint trained for 60000 epochs
* 4: checkpoint trained for 54000 epochs

By running `hw3_inference.sh` you can successfully finish the below workflow and generate a output.json.

(1) generate `test.json` which is a dummy file listing all test images.

(2) run `test_net.py` to generate predictions (bbox coordinate `[x, y, w, h]`)

(3) convert `bbox.json` to the format which matches the requirement of this homework (bbox coordinate `[xmin, ymin, xmax, ymax]`).

Note: all the path in `hw3_inference.sh` should be carefully modified before running.

### Visualize MIC Results
Here we plot mAP graphs and save them to `png` files at current working directory.
Adjust the model number in `run_all_eval.sh` according to the model weights you have.
```
./run_all_eval.sh /path/to/models
# e.g., ./run_all_eval.sh models/model_0523
```

### Training 
Please refer to [train.md](train.md)

## YOLOv5 (for Task 1)
`cd yolov5` to move to the correct working dir.

### Evaluation on **target**  dataset
Suppose we have our dataset in `path/to/fog_dataset`. Then, do the following modification in `foggy_cityscape.yaml`
```
# original
# path: /home/guest/r11944026/cv/hw3/data/hw3_dataset/

# new
path: /path/to/fog_dataset
```

Also, under `/path/to/dataset`, data should be put in the structure below.
```
/path/to/fog_dataset
    - images
        - train
            - *.png
        - val
            - *.png
```

Create labels for each evaluation image first. Then, do evaluation on **target** dataset (upon request).
```
python create_yolo_labels_for_single_file.py /path/to/fog_val.coco.json path/to/fog/labels
python val.py --weights path/to/best.pt --data foggy_cityscape.yaml --img 1024

# e.g., 
# python create_yolo_labels_for_single_file.py ~/cv/hw3/data/hw3_dataset/fog/val.coco.json ~/cv/hw3/data/hw3_dataset/fog/labels
# python val.py --weights runs/train/exp16/weights/best.pt --data foggy_cityscape.yaml --img 1024
```

### Training on source dataset
Please refer to [train.md](train.md)

### Debug
Suppose some weird bug happen, remember to check if there's any `train.cache` or `valid.cache` inside any yolo folders. Removing it can possibly fix the problem.

## Data
### Input
A json file which contains
* keys: 'categories', 'images', 'annotations'
* inside 'categories': a list of dict, where each element is `{'id': 1, 'name': 'person'}`, mapping id to class names.
* inside 'images': a list of dict, where each dict is sth like `{'id': 0, 'width': 2048, 'height': 1024, 'file_name': 'org/train/0000.png'}`, indicating information of each file.
* inside 'annotations': a list of dict, where each dict is sth like `{'id': 0, 'image_id': 905, 'category_id': 1, 'iscrowd': 0, 'area': 3212, 'bbox': [1251, 362, 49, 113]}`, indicating information of each bbox.

Size of 
* Org train: 2575 images
* Fog train: 2575 images
* Org val: 300 images (id: 0~299)
* Fog val: 300 images (id: 0~299)
* Fog test: 300 images (id: 0~299)

### Output Formatting
Ways to format predictions can be seen [here](https://github.com/facebookresearch/maskrcnn-benchmark/issues/327).

