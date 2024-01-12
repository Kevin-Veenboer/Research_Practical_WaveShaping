import tifffile as tiff
import matplotlib.pyplot as plt
import cv2
import os
from Focus_grid_constructor import generate_grid

path = "Tiffs/Phases/3/move_zstage00001_Measure0001.tif"

# The variable over takes a tuple with ((x_centre,y_centre), radius)

grid = generate_grid()


def TiffShow(path, multiples=True, save=False, cover=None):
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

            # Show image
            plt.imshow(image_color, cmap="gray" if image.ndim == 2 else None)
            plt.show()


TiffShow(path)
