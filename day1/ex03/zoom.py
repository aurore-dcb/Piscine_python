from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def zoom(array: list):
    center_x, center_y = array.shape[1] // 2, array.shape[0] // 2
    zoom_size = 400
    zoomed_image = array[center_y - zoom_size//2:center_y + zoom_size//2,
                         center_x - zoom_size//2:center_x + zoom_size//2, :]
    gray_image = Image.fromarray(zoomed_image).convert('L')
    zoomed_image_gray = np.array(gray_image)
    new_arr = zoomed_image_gray.reshape(zoom_size, zoom_size, 1)
    print("New shape after slicing:", new_arr.shape, "or", zoomed_image_gray.shape)
    np.set_printoptions(threshold=6, edgeitems=3, formatter={'int': '{:3}'.format})
    print(new_arr[:1])
    return new_arr

def main():
    try:
        arr = ft_load("../animal.jpeg")
    except:
        print("Error: something went wrong while loading the image.")
        return
    try:    
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        zoom_image = zoom(arr)
    except:
        
        print("Error: something went wrong while zoomig.")
        return
    try:
        axes[0].imshow(arr)
        axes[0].set_title('Original Image')
        axes[1].imshow(zoom_image, cmap='gray')
        axes[1].set_title('Zoomed Image')
        
        plt.tight_layout()
        plt.show()
    except:
        print("Error: something went wrong while displaying the image.")
        return

if __name__ == "__main__":
    main()
