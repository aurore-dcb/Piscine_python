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
    shape = array.shape
    rotate_image = np.zeros((shape[1], shape[0], shape[2]), dtype=np.uint8)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            rotate_image[j][i] = array[i][j]
    return rotate_image


def main():
    zoom_size = 400
    try:
        arr = ft_load("../animal.jpeg")
        zoomed_image = zoom(arr, zoom_size)
        gray_image = ft_gray(zoomed_image)
        np.set_printoptions(threshold=100, edgeitems=3)
        print("The shape of image is:", gray_image.shape, end=" ")
        print("or ", np.squeeze(gray_image).shape)
        print(gray_image[:1])
        rotate_image = np.squeeze(rotate(gray_image))
        print("New shape after Transpose:", np.squeeze(rotate_image).shape)
        print(rotate_image)
    except Exception as e:
        print(f"Error: something went wrong: {e}")
        exit(1)
    try:
        fig, axes = plt.subplots(2, 2, figsize=(12, 12))
        axes[0][0].imshow(arr)
        axes[0][0].set_title('Original Image')
        axes[0][1].imshow(zoomed_image)
        axes[0][1].set_title('Zoomed Image')
        axes[1][0].imshow(gray_image, cmap='gray')
        axes[1][0].set_title('Gray Image')
        axes[1][1].imshow(rotate_image, cmap='gray')
        axes[1][1].set_title('Rotate Image')
        plt.tight_layout
        plt.show()
    except Exception as e:
        print(f"Error: something went wrong while displaying the image: {e}")
        exit(1)


if __name__ == "__main__":
    main()
