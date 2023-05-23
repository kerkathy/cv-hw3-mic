"""
Extract mAP@[50:5:95], mAP@50, mAP@75 of different epochs from <path_to_model>/<epoch_num>/inference/my_cityscapes_test/coco_results.pth
where *.pth indicates the epoch number
And draw the map curve

Usage:
    python draw_map.py --model_path /path/to/model
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import torch
import argparse

def draw_map(metric='AP50', model_path='results'):
    vals = []
    epochs = []

    for epoch in os.listdir(model_path):
        # epoch should be an integer
        if not epoch.split('.')[0].isdigit() or not os.path.isdir(os.path.join(model_path, epoch)):
            continue
        epochs.append(int(epoch.split('.')[0]))
        path = os.path.join(model_path, epoch, 'inference', 'my_cityscapes_test', 'coco_results.pth')
        if not os.path.exists(path):
            print(f'{path} does not exist')
            continue
        coco_results = torch.load(path)
        vals.append(coco_results.results['bbox'][metric])

    # Sort the AP50 and epochs
    vals = np.array(vals)
    epochs = np.array(epochs)
    idx = np.argsort(epochs)
    epochs = epochs[idx]
    vals = vals[idx]
    print(f'epochs: {epochs}')
    print(f'{metric}: {vals}')

    # Draw the map curve
    plt.plot(epochs, vals)
    plt.xlabel('Epoch')
    plt.ylabel(f'{metric}')
    plt.title(f'{metric} of different epochs')

    # Save the figure
    plt.savefig(f'{metric}_curve.png')
    print(f'The map curve has been saved to {metric}_curve.png\n')

    # clear the figure
    plt.clf()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_path', type=str, required=True, help='Path to the model')
    args = parser.parse_args()

    metrics = ['AP', 'AP50', 'AP75']
    for mt in metrics:
        draw_map(mt, args.model_path)

if __name__ == '__main__':
    main()
