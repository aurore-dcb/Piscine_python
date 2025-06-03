import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def ft_invert(array) -> list:
    """ Inverts the color of the image received. """
    img = np.zeros((array.shape[0], array.shape[1], array.shape[2]), dtype="uint8")
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            for k in range(3):
                img[i,j,k] = 255 - array[i,j,k]
    plt.imshow(img)
    plt.show()
    return

def ft_red(array) -> list:
    """ Put a red filter on the image. """
    img = np.zeros((array.shape[0], array.shape[1], array.shape[2]), dtype="uint8")
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            img[i,j,0] = array[i,j,0]
            img[i,j,1] = 0
            img[i,j,2] = 0
    plt.imshow(img)
    plt.show()
    return

def ft_green(array) -> list:
    """ Put a green filter on the image. """
    img = np.zeros((array.shape[0], array.shape[1], array.shape[2]), dtype="uint8")
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            img[i,j,0] = 0
            img[i,j,1] = array[i,j,1]
            img[i,j,2] = 0
    plt.imshow(img)
    plt.show()
    return

def ft_blue(array) -> list:
    """ Put a blue filter on the image. """
    img = np.zeros((array.shape[0], array.shape[1], array.shape[2]), dtype="uint8")
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            img[i,j,0] = 0
            img[i,j,1] = 0
            img[i,j,2] = array[i,j,2]
    plt.imshow(img)
    plt.show()
    return

def ft_grey(array) -> list:
    """ Put a grey filter on the image. """
    img = np.zeros((array.shape[0], array.shape[1], array.shape[2]), dtype="uint8")
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            r, g, b = array[i,j,0], array[i,j,0], array[i,j,0]
            moyenne = (int(r) + int(g) + int(b)) // 3
            img[i,j] = [moyenne] * 3
            # for k in range(3):
            #     img[i,j,k] = ((array[i,j,0] + array[i,j,1] + array[i,j,2]) // 3)
    plt.imshow(img)
    plt.show()
    return