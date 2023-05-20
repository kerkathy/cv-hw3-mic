"""
Convert bbox.json to output.json using id2name.json
which contains the format of the submission

bbox.json looks like [{"image_id": id, "categoty_id": label, "bbox": [x1, y1, w, h], "score": score}, ...]
output.json looks like "<img file name>": {"boxes": [[x1, y1, x2, y2], ...], "labels": [label1, ...] , "scores": [score1, ...]}

and the correspondence between image file name and image id is in the file id2name.json
id2name.json looks like {"image_id": id, "file_name": "<img file name>"}
"""

import json
import argparse
from tqdm import tqdm

def parse_args():
    parser = argparse.ArgumentParser(description='Convert bbox.json to output.json')
    parser.add_argument('--bbox', required=True, help='bbox.json file path', type=str)
    parser.add_argument('--id2name', required=True, help='id2name.json file path', type=str)
    parser.add_argument('--output', required=True, help='output.json file path', type=str)
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    with open(args.bbox, 'r') as f:
        bbox = json.load(f)
    with open(args.id2name, 'r') as f:
        id2name = json.load(f)
    output = {}
    for img in tqdm(bbox):
        img_id = img['image_id']
        img_name = id2name[str(img_id)]
        if img_name not in output:
            output[img_name] = {'boxes': [], 'labels': [], 'scores': []}
        # convert bbox from [x, y, w, h] to [xmin, ymin, xmax, ymax]
        bbox = img['bbox']
        bbox[2] += bbox[0]
        bbox[3] += bbox[1]
        output[img_name]['boxes'].append(bbox)
        output[img_name]['labels'].append(img['category_id'])
        output[img_name]['scores'].append(img['score'])
    with open(args.output, 'w') as f:
        json.dump(output, f, indent=4)
        print('Write to {}. Image id\'s converted according to {}'.format(args.output, args.id2name))

if __name__ == '__main__':
    main()
