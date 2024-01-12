from PIL import Image, ImageDraw
import tifffile as tiff
import matplotlib.pyplot as plt
import cv2
import numpy as np

def get_SBR(image):
    # Define the focus region (for example, a small square around the focus point)
    focus_x, focus_y = 614, 610  # Focus point coordinates
    focus_size = 10  # Size of the focus region
    focus_region = image[focus_y-focus_size:focus_y+focus_size, focus_x-focus_size:focus_x+focus_size]

    # Define the background region
    # Ensure this region is representative of the background and free of special features
    bg_x, bg_y = 50, 50  # Starting coordinates for background region
    bg_size = 20  # Size of the background region
    background_region = image[bg_y:bg_y+bg_size, bg_x:bg_x+bg_size]

    # Calculate average intensities
    average_focus_intensity = np.mean(focus_region)
    average_background_intensity = np.mean(background_region)

    # Calculate contrast
    contrast = average_focus_intensity - average_background_intensity

    # Calculate SNR
    # SNR = Signal (mean of focus) / Noise (standard deviation of background)
    snr = average_focus_intensity / np.std(background_region)

    print(f"Average Focus Intensity: {average_focus_intensity}")
    print(f"Average Background Intensity: {average_background_intensity}")
    print(f"Contrast: {contrast}")
    print(f"Signal-to-Noise Ratio (SNR): {snr}")


image = tiff.imread('Tiffs/Phases/3/move_zstage00001_Measure0001.tif', series=0)
x_center, y_center = 614, 610

focus_center = image[12]
pixel_value_center = focus_center[y_center, x_center]

print(pixel_value_center)
get_SBR(image)

