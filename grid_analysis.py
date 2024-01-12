import tifffile as tiff
import numpy as np
import matplotlib.pyplot as plt
import cv2
from focus_grid_constructor import generate_grid


data_folder_phases = "./TIFFs/Phases/"
data_folder_segments = "./TIFFs/Segment/"

data_path_test = "./TIFFs/Phases/3/move_zstage00001_Measure0002.tif"


def get_focus_intensity(
    images,
    coords,
    cable_centre=(614, 610),
    cable_radius=550,
    focus_masking_radius=70,
    focus_radius=10,
):
    assert images.shape[0] == len(
        coords
    ), "Number of focus coordinates needs to equal number of images"

    image_height = images.shape[1]
    image_width = images.shape[2]

    data_dict = {"index": list(range(25)), "intensity": []}

    image_x, image_y = np.meshgrid(
        np.linspace(0, image_height - 1, image_height),
        np.linspace(0, image_width - 1, image_width),
    )

    background_mask = (image_x - cable_centre[0]) ** 2 + (
        image_y - cable_centre[1]
    ) ** 2 < cable_radius**2

    for image, coord in zip(images, coord):
        pass


def read_image_data(path):
    return tiff.imread(path)
