"""
Create a test.json file for inferencing.
The format should look like val.coco.json
where the images are in the directory specified by command line argument

also create a id2name.json file for inferencing
"""

import argparse
import json
import os
import random
import shutil
import sys

from tqdm import tqdm

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, required=True)
    parser.add_argument('--output_json', type=str, required=True, help='Name of output json file')
    parser.add_argument('--output_id2name', type=str, required=True, help='Name of output id2name json file')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()

    # Create a test json file
    test_json = {
        'categories': [
            {
                "id": 1,
                "name": "person"
            },
            {
                "id": 2,
                "name": "car"
            },
            {
                "id": 3,
                "name": "truck"
            },
            {
                "id": 4,
                "name": "bus"
            },
            {
                "id": 5,
                "name": "rider"
            },
            {
                "id": 6,
                "name": "motorcycle"
            },
            {
                "id": 7,
                "name": "bicycle"
            },
            {
                "id": 8,
                "name": "train"
            }
        ],
        'images': [],
        'annotations': [],
    }

    # Get all images in the directory
    image_paths = []
    subdir = "fog/public_test"
    test_dir = os.path.join(args.dataset, subdir)
    for root, _, files in os.walk(test_dir):
        for file in files:
            image_paths.append(os.path.join(root, file))

    id2names = {}

    # Add images to the json file
    for image_id, image_path in enumerate(tqdm(image_paths)):
        image = {
            'id': image_id,
            'width': 2048,
            'height': 1024,
            'file_name': os.path.abspath(image_path),
        }
        test_json['images'].append(image)
        id2names[image_id] = os.path.join(subdir, os.path.basename(image_path))

    # Write the json file with indent=4
    with open(args.output_json, 'w') as f:
        json.dump(test_json, f, indent=4)
        print('Created {}'.format(args.output_json))

    # Write the id2name json file with indent=2
    with open(args.output_id2name, 'w') as f:
        json.dump(id2names, f, indent=4)
        print('Created {}'.format(args.output_id2name))

if __name__ == '__main__':
    main()