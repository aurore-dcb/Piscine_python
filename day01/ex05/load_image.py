import numpy as np
from PIL import Image, UnidentifiedImageError


def ft_load(path: str) -> list:
    """ Load the given image as an Image object \
        and Print the format and pixels content"""
    try:
        assert isinstance(path, str)
    except AssertionError:
        raise TypeError("The path in ft_load(path) must be a string.")
    try:
        array = np.asarray(Image.open(path))
    except (UnidentifiedImageError, FileNotFoundError, PermissionError):
        raise Exception("Cannot open image: " + path)
    return array
