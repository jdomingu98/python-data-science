import numpy as np
import cv2


def ft_invert(array) -> np.array:
    """
    Inverts the color of the image received.
    """
    copy = 255 - array.copy()
    img = cv2.cvtColor(copy, cv2.COLOR_RGB2BGR)
    cv2.imshow("Inverted image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return copy


def ft_red(array) -> np.array:
    """
    Show only the red channel color of the image received.
    """
    copy = array.copy()
    copy[:, :, 1] = 0
    copy[:, :, 2] = 0
    img = cv2.cvtColor(copy, cv2.COLOR_RGB2BGR)
    cv2.imshow("Redscale image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return copy


def ft_green(array) -> np.array:
    """
    Show only the green channel color of the image received.
    """
    copy = array.copy()
    copy[:, :, 0] = 0
    copy[:, :, 2] = 0
    img = cv2.cvtColor(copy, cv2.COLOR_RGB2BGR)
    cv2.imshow("Greenscale image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return copy


def ft_blue(array) -> np.array:
    """
    Show only the blue channel color of the image received.
    """
    copy = array.copy()
    copy[:, :, 0] = 0
    copy[:, :, 1] = 0
    img = cv2.cvtColor(copy, cv2.COLOR_RGB2BGR)
    cv2.imshow("Bluescale image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return copy


def ft_grey(array) -> np.array:
    """
    Show the image received in grayscale.
    """
    copy = array.copy()
    copy = copy[:, :, 0] // 3 + copy[:, :, 1] // 3 + copy[:, :, 2] // 3
    img = cv2.cvtColor(copy, cv2.COLOR_RGB2BGR)
    cv2.imshow("Grayscale image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return copy
