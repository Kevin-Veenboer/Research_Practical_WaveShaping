import tifffile as tiff
import numpy as np
import matplotlib.pyplot as plt
import cv2
from focus_grid_constructor import generate_grid


data_folder_phases = "./TIFFs/Phases/"
data_folder_segments = "./TIFFs/Segment/"

data_path_test = "./TIFFs/Phases/3/move_zstage00001_Measure0002.tif"


def get_focus_intensity(images, coords):
    assert images.shape[0] == len(
        coords
    ), "Number of focus coordinates needs to equal number of images"

    for image, coord in zip(images):
        pass


def read_image_data(path):
    return tiff.imread(path)


grid_coordinates = generate_grid()


print(tiff.imread(data_path_test)[0])
