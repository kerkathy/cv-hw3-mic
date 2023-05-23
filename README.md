# cv-hw3-mic
Forked from MIC. Unsupervised domain adaptation using mic repo.

## Environment
Please follow the instruction in [INSTALL.md](MIC/det/INSTALL.md) to install and use this repo.
For installation problems, please consult issues in maskrcnn-benchmark .

## Inference
```
./hw3_inference.sh
```

By running `hw3_inference.sh` you can successfully finish the below workflow and generate a output.json.

(1) generate `test.json` which is a dummy file listing all test images.

(2) run `test_net.py` to generate predictions (bbox coordinate `[x, y, w, h]`)

(3) convert `bbox.json` to the format which matches the requirement of this homework (bbox coordinate `[xmin, ymin, xmax, ymax]`).

Note: all the path in `hw3_inference.sh` should be carefully modified before running.

## Some Notes for Training
`MIC/det/maskrcnn_benchmark/config/paths_catalog.py`: where the configuration key-value pairs are set.
`MIC/det/configs/da_faster_rcnn/<some_yaml_file>`: the actual configuration file
* when `train_net.py` is run, `DATASETS/SOURCE_TRAIN` and `DATASETS/TARGET_TRAIN` will be fetched.
* when `test_net.py` is run, `DATASETS/TEST` will be fetched.

## Data
### Input
A json file which contains
* keys: 'categories', 'images', 'annotations'
* inside 'categories': a list of dict, where each element is `{'id': 1, 'name': 'person'}`, mapping id to class names.
* inside 'images': a list of dict, where each dict is sth like `{'id': 0, 'width': 2048, 'height': 1024, 'file_name': 'org/train/0000.png'}`, idicating information of each file.
* inside 'annotations': a list of dict, where each dict is sth like `{'id': 0, 'image_id': 905, 'category_id': 1, 'iscrowd': 0, 'area': 3212, 'bbox': [1251, 362, 49, 113]}`, indicating information of each bbox.

Size of 
* Org train: 2575 images
* Fog train: 2575 images
* Org val: 300 images (id: 0~299)
* Fog val: 300 images (id: 0~299)
* Fog test: 300 images (id: 0~299)
### Output
Ways to format predictions can be seen [here](https://github.com/facebookresearch/maskrcnn-benchmark/issues/327).

