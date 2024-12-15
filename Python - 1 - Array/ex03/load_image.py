import numpy as np
import cv2


def ft_load(path: str) -> np.array:
    """
    This function loads an image from the given path, prints its format, and
    returns its pixel content in RGB format as a NumPy array.

    Parameters:
    - path: The file path to the image.

    Returns:
    The image's pixel content in RGB format.
    """
    assert (
        path.lower().endswith((".jpg", ".jpeg"))
    ), "Only JPG and JPEG formats are supported."
    img = cv2.imread(path)

    assert img is not None, "Invalid file path."

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    print(f"The shape of image is: {img.shape}")
    print(img)
