import tifffile as tiff
import matplotlib.pyplot as plt
import cv2

path = "Tiffs/Baseline/DO_phase_test_speckle_after_measure.tif"


def TiffShow(path):
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

            # Show image
            plt.imshow(image_color, cmap="gray" if image.ndim == 2 else None, norm=norm)
            plt.show()


TiffShow(path)
