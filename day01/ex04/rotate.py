from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def zoom(array: list, zoom_size: int) -> list:
    """ Extracts a square centered from the given image of a size equals to 'zoom_size' pixels. """
    center_x, center_y = array.shape[1] // 2, array.shape[0] // 2
    zoomed_image = array[center_y - zoom_size//2:center_y + zoom_size//2,
                         center_x - zoom_size//2:center_x + zoom_size//2, :]
    gray_image = Image.fromarray(zoomed_image).convert('L')
    zoomed_image_gray = np.array(gray_image)
    new_arr = zoomed_image_gray.reshape(zoom_size, zoom_size, 1)
    print("The shape of image is:", new_arr.shape, "or", zoomed_image_gray.shape)
    np.set_printoptions(threshold=6, edgeitems=3, formatter={'int': '{:3}'.format})
    print(new_arr[:1])
    return new_arr

def rotate(array: list) -> list:
    """ Rotate the given image 90 degrees to the left """
    zoomed_image = array.reshape(array.shape[0], array.shape[1])
    rotate_image = np.zeros((zoomed_image.shape[0], zoomed_image.shape[1]), dtype=np.uint8)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            rotate_image[399 - j][i] = zoomed_image[i][j]
    print("New shape after Transpose:", rotate_image.shape)
    np.set_printoptions(threshold=6, edgeitems=3, formatter={'int': '{:3}'.format})
    print(rotate_image)
    return rotate_image

def main():
    try:
        arr = ft_load("../animal.jpeg")
    except:
        print("Error: something went wrong while loading the image.")
        return
    try:
        zoom_image = zoom(arr, 400)
    except:
        print("Error: something went wrong while zooming.")
        return
    try:
        rotate_image = rotate(zoom_image)
    except:
        print("Error: something went wrong while rotating.")
        return
    try:
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        axes[0].imshow(zoom_image, cmap='gray')
        axes[0].set_title('Zoomed Image')
        axes[1].imshow(rotate_image, cmap='gray')
        axes[1].set_title('Rotate Image')
        plt.tight_layout
        plt.show()
    except:
        print("Error: something went wrong while displaying the image.")
        return
    return

if __name__ == "__main__":
    main()