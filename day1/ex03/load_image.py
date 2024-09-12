import numpy as np
from PIL import Image

def ft_load(path: str) -> list:
    try:
        img = Image.open(path)
    except:
        print("Error:", "cannot open image")
        return
    array = np.array(img)
    print("The shape of image is:", array.shape)
    print(array[0,:3])
    print("...")
    print(array[-1,-3:])
    return array

