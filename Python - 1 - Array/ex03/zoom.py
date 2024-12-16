import cv2
from load_image import ft_load


def main():
    """
    Load an image, print information, and display it zoomed.
    """
    img = ft_load("animal.jpeg")
    print(img)

    zoomed = img[:400, :400, :1]
    print(f"New shape after slicing:{zoomed.shape} or {zoomed.shape[:2]}")
    print(zoomed)

    # Display the image with axis labels
    zoomed_img_bgr = cv2.cvtColor(zoomed, cv2.COLOR_RGB2BGR)
    cv2.imshow("Zoomed Image", zoomed_img_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
