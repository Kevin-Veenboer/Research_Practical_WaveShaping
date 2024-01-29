import tifffile as tiff
import matplotlib.pyplot as plt
import cv2
import os
from focus_grid_constructor import generate_grid

path = "Tiffs/Phases/3/move_zstage00001_Measure0001.tif"
path_2 = "./TIFFs/Baseline/First_measurement.tif"
path_3 = "./TIFFs/Segments/30/move_zstage00001_Measure0003.tif"

store = "./temp/"
indexes = list(range(0, 25))

# The variable over takes a tuple with ((x_centre,y_centre), radius)

grid = generate_grid()[::-1]


def TiffShow(path, multiples=True, save=False, cover=None, Store=False):
    # open tiff file
    with tiff.TiffFile(path) as tif:
        layers = tif.pages

        # Loop over layer and display images
        for page in layers:
            image = page.asarray()

            # check for color
            if len(image.shape) == 2:  # Gray
                image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
            else:
                image_color = image

            coords = grid.pop()
            cv2.circle(image_color, tuple(coords), 4, (255, 0, 0), -1)

            cv2.circle(image_color, (614, 610), 550, (255, 0, 0), 3)

            if Store:
                cv2.imwrite(store + f"img_{indexes.pop()}.tif", image)

            # Show image
            plt.imshow(image_color, cmap="gray" if image.ndim == 2 else None)
            plt.show()


TiffShow(path_3, Store=True)
