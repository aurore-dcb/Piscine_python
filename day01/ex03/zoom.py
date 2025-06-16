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


def main():
    zoom_size = 400
    try:
        arr = ft_load("../animal.jpeg")
        print("The shape of image is:", arr.shape)
        print(arr)
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        zoom_image = zoom(arr, zoom_size)
        gray_image = ft_gray(zoom_image)
        print("New shape after slicing:", gray_image.shape, end=" ")
        print("or", np.squeeze(gray_image).shape)
        print(gray_image)
        axes[0].imshow(arr)
        axes[0].set_title('Original Image')
        axes[1].imshow(gray_image, cmap='gray')
        axes[1].set_title('Zoomed Image')
        plt.show()
    except Exception as e:
        print(f"Error: something went wrong: {e}")
        exit(1)


if __name__ == "__main__":
    main()
