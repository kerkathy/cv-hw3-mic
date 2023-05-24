"""
Similar to create_test_json.py
but this script will create an overall test.json file for all subdirectories
"""

import argparse
import json
import os
from tqdm import tqdm

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, required=True)
    parser.add_argument('--output_json', type=str, required=True, help='Name of output json file')
    parser.add_argument('--output_id2name', type=str, required=True, help='Name of output id2name json file')
    parser.add_argument('--subdir_as_path', action='store_true', help='Use the path of the subdirectory as the image name')
    parser.add_argument('--dummy_bbox', action='store_true', help='Create dummy bounding boxes for each image')
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

    id2name = {}

    # Create a list of subdirectories
    subdirs = [subdir for subdir in os.listdir(args.dataset) if os.path.isdir(os.path.join(args.dataset, subdir))]
    subdirs.sort()

    # Iterate through each subdirectory
    for subdir in subdirs:
        print('Processing subdirectory {}'.format(subdir))
        # Create a list of images in the subdirectory
        images = [image for image in os.listdir(os.path.join(args.dataset, subdir)) if image.endswith('.png')]
        images.sort()

        # Iterate through each image
        for image in tqdm(images):
            # Create an entry for the image
            image_entry = {
                'id': len(test_json['images']),
                'width': 2048,
                'height': 1024,
                'file_name': os.path.join(subdir, image) if args.subdir_as_path else os.path.join(args.dataset, subdir, image),
            }
            test_json['images'].append(image_entry)

            # Create an entry for the annotation
            annotation_entry = {
                'id': len(test_json['annotations']),
                'image_id': image_entry['id'],
                'category_id': 1,
                'iscrowd': 0,
                'area': 3212,
                'bbox': [1251, 362, 49, 113], # fake but can't be all 0
            }
            test_json['annotations'].append(annotation_entry)

            # Create an entry for id2name, which maps image id to relative image name
            id2name[image_entry['id']] = os.path.join(subdir, image)

    # Write the test json file
    with open(args.output_json, 'w') as f:
        json.dump(test_json, f, indent=4)
        print('Created test json file at {}'.format(args.output_json))

    # Write the id2name json file
    with open(args.output_id2name, 'w') as f:
        json.dump(id2name, f, indent=4)
        print('Created id2name json file at {}'.format(args.output_id2name))

if __name__ == '__main__':
    main()