import tifffile as tiff
import numpy as np
import matplotlib.pyplot as plt
import cv2
from focus_grid_constructor import generate_grid
import pandas as pd
import time
from os import listdir

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
    """_summary_

    Args:
        images (ndarray): image data to be scanned
        coords (list): list with tuples containing coordinates of the focus spots
        cable_centre (tuple, optional): centre of the optical cable in the images. Defaults to (614, 610).
        cable_radius (int, optional): radius of the optical cable. Defaults to 550.
        focus_masking_radius (int, optional): radius of mask to cover focus spot when calculating the background signal. Defaults to 70.
        focus_radius (int, optional): radius of mask in which to determine the focus spot intensity. Defaults to 10.

    Returns:
        dict: dictionary containing the data per focus spot
    """
    assert images.shape[0] == len(
        coords
    ), "Number of focus coordinates needs to equal number of images"

    image_height = images.shape[1]
    image_width = images.shape[2]

    data_dict = {
        "index": list(range(25)),
        "focus_intensity": [],
        "background_intensity": [],
        "focus_std": [],
        "background_std": [],
    }

    image_x, image_y = np.meshgrid(
        np.linspace(0, image_height - 1, image_height),
        np.linspace(0, image_width - 1, image_width),
    )

    for image, coord in zip(images, coords):
        # Create a mask for background signal, include only the cable and exclude the focus
        background_mask = (
            (image_x - cable_centre[0]) ** 2 + (image_y - cable_centre[1]) ** 2
            < cable_radius**2
        ) & (
            (image_x - coord[0]) ** 2 + (image_y - coord[1]) ** 2
            > focus_masking_radius**2
        )

        # Create a mask for the focus spot signal
        focus_mask = (image_x - coord[0]) ** 2 + (
            image_y - coord[1]
        ) ** 2 < focus_radius

        # Apply masks to filter out data from the image
        background_data = image[background_mask]
        focus_data = image[focus_mask]

        # Store the intermediate results
        data_dict["focus_intensity"].append(np.mean(focus_data))
        data_dict["background_intensity"].append(np.mean(background_data))
        data_dict["focus_std"].append(np.std(focus_data))
        data_dict["background_std"].append(np.std(background_data))

    return data_dict


def read_image_data(path):
    return tiff.imread(path)


# start = time.time()
# image_data = read_image_data(data_path_test)
# focus_grid = generate_grid()
# test = pd.DataFrame(get_focus_intensity(image_data, focus_grid))
# end = time.time()
# print(f"One file to {end-start} seconds to process.\nThis means the phases will take about {19*(end-start)} seconds to process.\nThis means the phases will take about {29*(end-start)} seconds to process.")


print(listdir(data_folder_phases))
print(listdir(data_folder_phases + listdir(data_folder_phases)[0]))

focus_grid = generate_grid()


for phase in listdir(data_folder_phases):
    for image_file in listdir(data_folder_phases + phase):
        image_data = read_image_data(data_folder_phases + phase + "/" + image_file)
        data = get_focus_intensity(image_data, focus_grid)
