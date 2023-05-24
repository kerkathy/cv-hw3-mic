# Training Instruction
## MIC
In this section, we are going to train MIC object detection model using domain adaptive method on cityscapes dataset.

You should have the following data on hand.
* training data on source domain (`org` for cityscapes dataset); **with annotation** `train_org.coco.json`
* training data on target domain (`foggy` for cityscapes dataset); this can be without annotation
* validation data on target domain (`foggy` for cityscapes dataset); **with annotation** `val.coco.json`

### Before we start
Data should be store in the following structure under main data directory `/path/to/dataset`
```
/path/to/dataset
    - org
        - train
            - *.png
        - val
            - *.png
    - fog
        - train
            - *.png
        - val
            - *.png
```

Since the data on target domain is assumed to have no label, we need to generate a fake annotation file `train_fog.coco.json` in order to run the script. 
```
python create_test_json.py --dataset /path/to/dataset --subdir fog/train --output_json train_fog.coco.json --output_id2name id2name_fog_train.json --subdir_as_path --dummy_bbox
```

### Modification
Modify the following section in [paths_catalog.py](MIC/det/maskrcnn_benchmark/config/paths_catalog.py). 
```
        "my_cityscapes_train": {
            "img_dir": "/home/guest/r11944026/cv/hw3/data/hw3_dataset",
            "ann_file": "/home/guest/r11944026/cv/hw3/data/hw3_dataset/org/train.coco.json"
        },
        "my_foggy_cityscapes_train": {
            "img_dir": "/home/guest/r11944026/cv/hw3/data/hw3_dataset",
            "ann_file": "/home/guest/r11944026/cv/hw3/data/hw3_dataset/fog/train_fog.json"
        },
        "my_cityscapes_test": {
            "img_dir": "/home/guest/r11944026/cv/hw3/data/hw3_dataset",
            "ann_file": "/home/guest/r11944026/cv/hw3/data/hw3_dataset/fog/val.coco.json"
        },
```
into
```
        "my_cityscapes_train": {
            "img_dir": "/path/to/dataset",
            "ann_file": "/path/to/train_org.coco.json"
        },
        "my_foggy_cityscapes_train": {
            "img_dir": "/path/to/dataset",
            "ann_file": "/path/to/train_fog.coco.json"
        },
        "my_cityscapes_test": {
            "img_dir": "/path/to/dataset",
            "ann_file": "/path/to/fog/val.coco.json"
        },
```

### Run Training
Simply run `hw3_train.sh` or the following.
```
python MIC/det/tools/train_net.py --config-file MIC/det/configs/da_faster_rcnn/e2e_da_faster_rcnn_R_50_FPN_masking_cs.yaml 
```

### Some Notes for Training MIC
[paths_catalog.py](MIC/det/maskrcnn_benchmark/config/paths_catalog.py) is where the configuration key-value pairs are set.

[e2e_da_faster_rcnn_R_50_FPN_masking_cs.yaml](MIC/det/configs/da_faster_rcnn/e2e_da_faster_rcnn_R_50_FPN_masking_cs.yaml) and [my_test.yaml](MIC/det/configs/da_faster_rcnn/my_test.yaml) are the actual configuration file
* when `train_net.py` is run, `DATASETS/SOURCE_TRAIN` and `DATASETS/TARGET_TRAIN` will be fetched.
* when `test_net.py` is run, `DATASETS/TEST` will be fetched.

### Pretrained weight
According to [path_catalog.py](MIC/det/maskrcnn_benchmark/config/paths_catalog.py) and [e2e_da_faster_rcnn_R_50_FPN_masking_cs.yaml](MIC/det/configs/da_faster_rcnn/e2e_da_faster_rcnn_R_50_FPN_masking_cs.yaml), the pretrained weight can be accessed [here](https://dl.fbaipublicfiles.com/detectron/ImageNetPretrained/MSRA/R-50.pkl).


## YOLO
### Before we start
Here we aren't going to do domain adaptation. Thus, we are only going to use source dataset to train the yolo model. Now we need to organize the data in specific format.

Suppose we have our dataset in `path/to/dataset`. Then, do the following modification in `cityscape.yaml`
```
# original
# path: /home/guest/r11944026/cv/hw3/data/hw3_dataset/

# new
path: /path/to/dataset
```

Also, under `/path/to/dataset`, data should be put in the structure below.
```
/path/to/dataset
    - images
        - train
            - *.png
        - val
            - *.png
```

Next, create labels that matches yolo txt format from existing annotation file `train.coco.json`. 
```
python create_yolo_labels_for_single_file.py /path/to/train.coco.json /path/to/dataset/labels
python create_yolo_labels_for_single_file.py /path/to/val.coco.json /path/to/dataset/labels

# e.g., 
# python create_yolo_labels_for_single_file.py ~/cv/hw3/data/hw3_dataset/org/train.coco.json ~/cv/hw3/data/hw3_dataset/labels
# python create_yolo_labels_for_single_file.py ~/cv/hw3/data/hw3_dataset/org/val.coco.json ~/cv/hw3/data/hw3_dataset/labels
```

To this end, the file structure should look like this and should be fine for training.
```
/path/to/dataset
    - images
        - train
            - *.png
        - val
            - *.png
    - labels
        - train
            - *.txt
        - val
            - *.txt
```


For more details, please consult [the official page](https://docs.ultralytics.com/yolov5/tutorials/train_custom_data/)

### Run Training
```
python train.py --data cityscape.yaml
```