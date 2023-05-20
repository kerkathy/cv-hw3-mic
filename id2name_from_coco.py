"""
Create a dictionary of id to name from COCO dataset
"""

import json
import argparse
from tqdm import tqdm

def parse_args():
    parser = argparse.ArgumentParser(description='Create a dictionary of id to name from COCO dataset')
    parser.add_argument('--coco', help='coco.json file path', default='coco.json', type=str)
    parser.add_argument('--output', help='output.json file path', default='id2name.json', type=str)
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    with open(args.coco, 'r') as f:
        coco = json.load(f)
    id2name = {}
    for img in tqdm(coco['images']):
        id2name[str(img['id'])] = img['file_name']
    with open(args.output, 'w') as f:
        json.dump(id2name, f, indent=4)
        print('Write to {}'.format(args.output))

if __name__ == '__main__':
    main()