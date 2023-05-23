"""
Extract mAP@[50:5:95], mAP@50, mAP@75 of different epochs from results/*.pth
where *.pth indicates the epoch number
And draw the map curve
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import torch

def draw_map(metric='AP50'):
    # Read the AP50 from results/*.pth
    vals = []
    epochs = []
    for file in os.listdir('results'):
        if file.endswith('.pth'):
            epochs.append(int(file.split('.')[0]))
            vals.append(torch.load(os.path.join('results', file))['bbox'][metric])

    # Sort the AP50 and epochs
    vals = np.array(vals)
    epochs = np.array(epochs)
    idx = np.argsort(epochs)
    epochs = epochs[idx]
    vals = vals[idx]

    # Draw the map curve
    plt.plot(epochs, vals)
    plt.xlabel('Epoch')
    plt.ylabel(f'{metric}')
    plt.title(f'{metric} of different epochs')

    # Save the figure
    plt.savefig('map_curve.png')
    print('The map curve has been saved to map_curve.png')

def main():
    metrics = ['AP', 'AP50', 'AP75']
    for mt in metrics:
        draw_map(mt)

if __name__ == '__main__':
    draw_map()

