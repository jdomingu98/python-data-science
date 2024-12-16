import numpy as np
import cv2
from load_image import ft_load


def main():
    """
    Load an image, print information, and display it rotated.
    """
    img = ft_load("animal.jpeg")

    cutted = img[:400, :400, :1]
    print(f"The shape of image is: {cutted.shape} or {cutted.shape[:2]}")
    print(cutted)

    transpose = np.zeros((cutted.shape[1], cutted.shape[0]),
                         dtype=cutted.dtype)
    for i in range(cutted.shape[0]):
        for j in range(cutted.shape[1]):
            transpose[j, i] = cutted[i, j]
    print(f"New shape after Transpose: {transpose.shape[:2]}")
    print(transpose)

    # Display the image with axis labels
    zoomed_img_bgr = cv2.cvtColor(transpose, cv2.COLOR_RGB2BGR)
    cv2.imshow("Rotated Image", zoomed_img_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
