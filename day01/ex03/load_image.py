import numpy as np
from PIL import Image


def ft_load(path: str) -> list:
    """ Load the given image as an Image object \
        and Print the format and pixels content"""
    array = np.asarray(Image.open(path))
    print("The shape of image is:", array.shape)
    print(array[0, :3])
    print("...")
    print(array[-1, -3:])
    return array
