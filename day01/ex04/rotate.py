from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def zoom(array: list, zoom_size: int) -> list:
    """ Extracts a square centered from the given image of a size \
        equals to 'zoom_size' pixels. """
    if zoom_size > array.shape[0] or zoom_size > array.shape[1]:
        zoom_size = min(array.shape[0], array.shape[1])
    center_x, center_y = array.shape[1] // 2, array.shape[0] // 2
    zoomed_image = array[center_y - zoom_size//2:center_y + zoom_size//2,
                         center_x - zoom_size//2:center_x + zoom_size//2, :]
    return zoomed_image

def ft_gray(array: list) -> list:
    """ Convert the given image to grayscale. """
    gray_image = Image.fromarray(array).convert('L')
    gray_array = np.asarray(gray_image)
    return gray_array.reshape(gray_array.shape[0], gray_array.shape[1], 1)


def rotate(array: list) -> list:
    """ Rotate the given image 90 degrees to the left """
    rotate_image = np.zeros((array.shape[0], array.shape[1], array.shape[2]), dtype=np.uint8)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            # tmp = zoomed_image[i][j]
            # rotate_image[i][j] = zoomed_image[j][i]
            rotate_image[array.shape[1] - 1 - j][i] = array[i][j]
    np.set_printoptions(threshold=6, edgeitems=3, formatter={'int': '{:3}'.format})
    # print(rotate_image)
    return rotate_image

def main():
    zoom_size = 400
    try:
        arr = ft_load("../animal.jpeg")
        # gray_image = ft_gray(arr)
        zoomed_image = zoom(arr, zoom_size)
        rotate_image = rotate(zoomed_image)
        print("New shape after Transpose:", rotate_image.shape)
    except Exception as e:
        print(f"Error: something went wrong: {e}")
        exit(1)
    try:
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        axes[0].imshow(zoomed_image, cmap='gray')
        axes[0].set_title('Zoomed Image')
        axes[1].imshow(rotate_image, cmap='gray')
        axes[1].set_title('Rotate Image')
        plt.tight_layout
        plt.show()
    except Exception as e:
        print(f"Error: something went wrong while displaying the image: {e}")
        exit(1)

if __name__ == "__main__":
    main()