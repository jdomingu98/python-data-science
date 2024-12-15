import cv2
from load_image import ft_load


def main():
    """
    Load an image, print information, and display it zoomed.

    Parameters:
    - path (str): The file path to the image.
    - scale_factor (float): The zoom factor (default is 2.0).
    """
    img = ft_load("animal.jpeg")
    print(img)

    zoomed_img = img[:400, :400, :1]
    print("New shape after slicing: (400, 400, 1) or (400, 400)")
    print(zoomed_img)

    # Display the image with axis labels
    zoomed_img_bgr = cv2.cvtColor(zoomed_img, cv2.COLOR_RGB2BGR)
    cv2.imshow("Zoomed Image", zoomed_img_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
