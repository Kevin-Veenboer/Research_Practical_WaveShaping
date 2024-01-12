from PIL import Image, ImageDraw
import tifffile as tiff
import matplotlib.pyplot as plt
import cv2
import numpy as np
from os import listdir
import pandas as pd

def get_average_focus(image, focus_x, focus_y, radius):
    n = 0
    total = 0
    for x in range(focus_x - radius, focus_x + radius):
        for y in range(focus_y - radius, focus_y + radius):
            if (x - focus_x)**2 + (y - focus_y)**2 > radius**2:
                total += image[x][y]
                n+=1
    return total / n

def get_average_background(image, focus_x, focus_y, radius):
    n = 0
    total = 0
    for x in range(200, 1000):
        for y in range(200, 1000):
            if (x - focus_x)**2 + (y - focus_y)**2 > radius**2:
                total += image[x][y]
                n+=1
    return total / n

def get_enhancement(image):
    # Define the focus region (for example, a small square around the focus point)
    focus_x, focus_y = 614, 610  # Focus point coordinates
    focus_size = 5  # Size of the focus region
    focus_region = image[focus_y-focus_size:focus_y+focus_size, focus_x-focus_size:focus_x+focus_size]

    # Define the background region
    # Ensure this region is representative of the background and free of special features
    bg_x, bg_y = 200, 200  # Starting coordinates for background region
    bg_size = 300  # Size of the background region
    background_region = image[bg_y:bg_y+bg_size, bg_x:bg_x+bg_size]

    # Calculate average intensities
    average_focus_intensity = np.mean(focus_region)
    average_focus_intensity2 = get_average_focus(image, focus_x, focus_y, 2)
    average_background_intensity = get_average_background(image, focus_x, focus_y, 40)

    enhancement = average_focus_intensity/average_background_intensity
    # Calculate contrast
    contrast = average_focus_intensity - average_background_intensity

    # Calculate SNR
    # SNR = Signal (mean of focus) / Noise (standard deviation of background)
    snr = average_focus_intensity / np.std(background_region)

    print(f"Average Focus Intensity: {average_focus_intensity}")
    print(f"Average Background Intensity: {average_background_intensity}")
    print(f"Enhancement: {enhancement}")
    print(f"Contrast: {contrast}")
    print(f"Signal-to-Noise Ratio (SNR): {snr}")
    return enhancement, average_focus_intensity, average_background_intensity

def get_middle_focus(file):
    image = tiff.imread(file, series=0)
    return image[12]

def main():
    data = {'Segments': [], 'Enhancement': [], 'Focus': [], 'Background': []}
    df = pd.DataFrame(data)
    for i in range(5, 31, 5):
        path = f"Tiffs/Segments/{i}/"
        files = listdir(path)
        enhancement = []
        for file in files:
            image = get_middle_focus(path+file)
            enhancement, focus, background = get_enhancement(image)
            df.loc[len(df.index)] =  [i, enhancement, focus, background]

    print(df)


if __name__ == "__main__":
    main()