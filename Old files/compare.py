from PIL import Image, ImageDraw
import tifffile as tiff
import matplotlib.pyplot as plt
import cv2

image = Image.open('TIFFs/Baseline/First_measurement.tif')
print(image.mode)

# Load the multi-layered TIFF image
multi_layered_image = tiff.imread('Tiffs/Phases/3/move_zstage00001_Measure0001.tif', series=0)  # series=0 for the first series if it's a multifile series

# Load the single-layered TIFF image
single_layered_image = tiff.imread('TIFFs/Baseline/First_measurement.tif')

x, y = 614, 610  # Replace with your coordinates

# Choose a specific layer, e.g., the first layer
specific_layer = multi_layered_image[12]  # Adjust the index for a different layer

# Extract the pixel values at the specified spot
pixel_value_multi = specific_layer[y, x]
pixel_value_single = single_layered_image[y, x]

# Compare and print the values
print(f"Pixel value in specific layer of multi-layered image: {pixel_value_multi}, Pixel value in single-layered image: {pixel_value_single}")

radius = 10  # Radius of the marker

# Choose a specific layer from the multi-layered image, e.g., the first layer
specific_layer = multi_layered_image[12]  # Adjust the index for a different layer


# Add a red dot marker at the specified spot
specific_layer_marked = specific_layer.copy()
single_layered_image_marked = single_layered_image.copy()

# Drawing a red dot on the images
specific_layer_marked[y-radius:y+radius, x-radius:x+radius] = 255  # Adjust color for your image type
single_layered_image_marked[y-radius:y+radius, x-radius:x+radius] = 255  # Adjust color for your image type

# Display the specific layer of the multi-layered image with the marker
plt.figure(figsize=(8, 8))
plt.imshow(specific_layer_marked, cmap='gray')
plt.title('Specific Layer of Multi-Layered Image with Marker')
plt.show()

# Display the single-layered image with the marker
plt.figure(figsize=(8, 8))
plt.imshow(single_layered_image_marked, cmap='gray')
plt.title('Single-Layered Image with Marker')
plt.show()