from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey
import matplotlib.pyplot as plt


def main():
    try:
        array = ft_load("../landscape.jpg")
        print(array)
        plt.imshow(array)
        plt.title('Original Image')
        plt.show()

        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)
    except Exception as e:
        print(f"Error: something went wrong: {e}")
        exit(1)
    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
