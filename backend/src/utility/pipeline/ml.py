import pickle

import numpy as np
import tensorflow as tf

from src.utility.enum.ml import MLModelLibrary


def load_model(ml_model_file, ml_library: str, custom_objects: dict | None = None):
    if ml_library.lower() == MLModelLibrary.TF:
        return tf.keras.models.load_model(filepath=ml_model_file, custom_objects=custom_objects)
    return pickle.loads(ml_model_file)


def predict(ml_model, ml_library: str, image_as_array: np.ndarray, th: float) -> np.ndarray:
    if ml_library.lower() == MLModelLibrary.TF:
        return ml_model.predict(x=image_as_array) > th
    return ml_model.predict(X=image_as_array) > th


def model_predict(
    ml_model_file, threshold: float, ml_library: str, image_as_array: np.ndarray, custom_objects: dict | None = None
):
    ml_model = load_model(ml_model_file=ml_model_file, ml_library=ml_library, custom_objects=custom_objects)
    return predict(ml_model=ml_model, ml_library=ml_library, image_as_array=image_as_array, th=threshold)
