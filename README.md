# cv-hw3-mic
Forked from MIC. Unsupervised domain adaptation using mic repo.

## Data

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
