from PIL import Image
import matplotlib.pyplot as plt

# Load the TIFF file
tiff_file = 'Tiffs/Phases/3/move_zstage00001_Measure0001.tif'
image = Image.open(tiff_file)

# Display image information
print("Mode:", image.mode)
print("Size:", image.size)

# Visualize the image
plt.imshow(image)
plt.show()