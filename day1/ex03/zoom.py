from load_image import ft_load
import matplotlib.pyplot as plt

def zoom(array: list):
    center_x, center_y = array.shape[1] // 2, array.shape[0] // 2
    zoom_size = 100
    zoomed_image = array[center_y - zoom_size//2:center_y + zoom_size//2,
                         center_x - zoom_size//2:center_x + zoom_size//2, :]
    print("new shape :", zoomed_image.shape)
    return zoomed_image

def main():
    arr = ft_load("../landscape.jpg")
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    axes[0].imshow(arr)
    axes[0].set_title('Original Image')

    zoom_image = zoom(arr)

    axes[1].imshow(zoom_image)
    axes[1].set_title('Zoomed Image')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
