import numpy as np
from PIL import Image, UnidentifiedImageError


def ft_load(path: str) -> list:
    """ Print the format and pixels content of a given image. """
    try:
        img = Image.open(path)
    except (UnidentifiedImageError, FileNotFoundError, PermissionError):
        print("Error:", "cannot open image")
        return
    array = np.asarray(img)
    print("The shape of image is:", array.shape)
    return array
