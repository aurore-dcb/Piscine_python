import numpy as np
from PIL import Image

def ft_load(path: str) -> list:
    """ Print the format and pixels content of a given image. """
    try:
        img = Image.open(path)
    except:
        print("Error:", "cannot open image")
        return
    array = np.array(img)
    print("The shape of image is:", array.shape)
    return array