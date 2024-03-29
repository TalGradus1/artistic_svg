import rembg
import numpy as np
from controlnet_aux import LineartDetector
from PIL import ImageOps, Image
import PIL


def remove_background(img_array: np.ndarray, alpha_matting: bool = False, alpha_matting_erode_size: int = 10,
                      alpha_matting_foreground_threshold: int = 240,
                      alpha_matting_background_threshold: int = 10) -> np.ndarray:
    """
    Removes the background from an image.
    :param img_array (np.ndarray): The image as a numpy array.
    :param alpha_matting (bool, optional): Flag indicating whether to use alpha matting. Defaults to False.
    :param alpha_matting_erode_size (int, optional): Erosion size for alpha matting. Defaults to 10.
    :param alpha_matting_foreground_threshold (int, optional): Foreground threshold for alpha matting. Defaults to 240.
    :param alpha_matting_background_threshold (int, optional): Background threshold for alpha matting. Defaults to 10.
    :return: (np.ndarray): The image without a background.
    """
    return rembg.remove(img_array, alpha_matting=alpha_matting, alpha_matting_erode_size=alpha_matting_erode_size,
                        alpha_matting_foreground_threshold=alpha_matting_foreground_threshold,
                        alpha_matting_background_threshold=alpha_matting_background_threshold)


def to_line_art(image: Image) -> Image:
    """
    Converts an image to line art using lllyasviel/Annotators model and returning the inverse.
    :param image (Image): The image to convert.
    :return: (Image): converted image
    """
    processor = LineartDetector.from_pretrained("lllyasviel/Annotators")
    control_image = processor(image)
    im_invert = ImageOps.invert(control_image)
    return im_invert
