from PIL import Image, ImageDraw
import tifffile as tiff
import matplotlib.pyplot as plt
import cv2

# Load the TIFF file
tiff_file = "Tiffs/Phases/3/move_zstage00001_Measure0001.tif"

with tiff.TiffFile("Tiffs/Phases/3/move_zstage00001_Measure0001.tif") as tif:
    layers = tif.pages
    num_layers = len(layers)
    print(f"The TIFF file has {num_layers} layers.")

    # Define the coordinates for the marker
    x, y = 614, 610  # Replace with your coordinates
    radius = 5
    color = (255, 0, 0)  # Red in RGB format
    thickness = -1  # Filled circle

    # Loop through each layer
    for i, page in enumerate(layers):
        image = page.asarray()

        # Check if the image is grayscale or color
        if len(image.shape) == 2:  # Grayscale image
            image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        else:  # Color image
            image_color = image

        # Draw the marker
        cv2.circle(image_color, (x, y), radius, color, thickness)

        plt.imshow(image_color, cmap="gray" if image.ndim == 2 else None)

        plt.title(f"Layer {i+1}")
        plt.show()
