import io

import numpy as np
import PIL.Image as PillowImage

from src.utility.enum.ml import MLModelLibrary, NNArchitecture


def open_image(image):
    new_image = PillowImage.open(io.BytesIO(initial_bytes=image))
    return new_image.convert(mode="RGBA")


def resize_image(image: PillowImage.Image):
    if image.size != (120, 120):
        return image.resize(size=(120, 120))
    return image


def image_to_array(image) -> np.ndarray:
    # PNGs have 4 channels and need adjustments
    if image.mode == "RGBA":
        # add white background
        white_bg = PillowImage.new(mode="RGBA", size=image.size, color=(255, 255, 255))
        image = PillowImage.alpha_composite(im1=white_bg, im2=image)

    # normalize to values between 0 and 1
    data = np.array(object=image)
    data = data.astype(dtype=np.float32) / 255

    # Invert colors
    data = 1 - data

    # Remove fourth channel, if it exists
    return data[:, :, :3]


def reshape_image_dimension(image: np.ndarray, ml_library: str, nn_type: str | None) -> np.ndarray:
    if ml_library == MLModelLibrary.TF:
        if nn_type == NNArchitecture.ANN:
            return image.reshape(image.shape[0], image.shape[1] * image.shape[2] * image.shape[3])
        reshaped_image = np.expand_dims(image, axis=0)
        return np.expand_dims(reshaped_image, axis=-1)
    return image.reshape(1, -1)


def prepare_image(image, ml_library: str, nn_type: str | None) -> np.ndarray:
    new_image = open_image(image=image)
    resized_image = resize_image(image=new_image)
    image_as_array = image_to_array(image=resized_image)
    return reshape_image_dimension(image=image_as_array, ml_library=ml_library, nn_type=nn_type)
