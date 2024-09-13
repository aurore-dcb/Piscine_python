import numpy as np
from PIL import Image

def ft_load(path: str) -> list:
    """ Load the given image as an Image object and return an array of its content. """
    try:
        img = Image.open(path)
    except:
        print("Error:", "cannot open image")
        return
    array = np.array(img)
    return array

