import numpy as np
from PIL import Image, UnidentifiedImageError


def ft_load(path: str) -> list:
    """ Print the format and pixels content of a given image. """
    try:
        assert isinstance(path, str)
    except AssertionError:
        print("Error: The path in ft_load(path) must be a string.")
        exit(1)
    try:
        img = Image.open(path)
    except (UnidentifiedImageError, FileNotFoundError, PermissionError):
        print("Error:", "cannot open image")
        exit(1)
    array = np.asarray(img)
    print("The shape of image is:", array.shape)
    return array
