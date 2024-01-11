import tifffile as tiff
import matplotlib.pyplot as plt
import cv2
import os

path = "Tiffs/Phases/3/move_zstage00001_Measure0001.tif"

# The variable over takes a tuple with ((x_centre,y_centre), radius)


# cover area :: ()

cover = ((210, 210), (1020, 1000))
color = (255, 0, 0)
thickness = 2


def TiffShow(path, multiples=True, save=False, cover=None):
    # open tiff file
    with tiff.TiffFile(path) as tif:
        layers = tif.pages if len(tif.pages) == 1 else list(tif.pages[12])

        # Loop over layer and display images
        for page in layers:
            image = page.asarray()

            # check for color
            if len(image.shape) == 2:  # Gray
                image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
            else:
                image_color = image

            # Set cover is needed
            if cover:
                cv2.rectangle(image_color, cover[0], cover[1], color, thickness)

            # Show image
            plt.imshow(image_color, cmap="gray" if image.ndim == 2 else None)
            plt.show()


# TiffShow(path, cover=cover)
with tiff.TiffFile(path) as tif:
    test = tif.pages
    print(repr(test))
    repr(test)

print(os.listdir(os.getcwd()))
