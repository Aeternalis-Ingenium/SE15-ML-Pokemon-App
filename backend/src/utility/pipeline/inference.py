import numpy as np

from src.utility.pipeline.image_processing import prepare_image
from src.utility.pipeline.ml import model_predict


async def inference_pipeline(
    pokemon_image_as_bytes,
    ml_model_as_bytes,
    threshold: float | None,
    ml_library: str,
    nn_type: str | None,
    custom_objects: dict | None = None,
) -> np.ndarray:
    image_as_array = prepare_image(image=pokemon_image_as_bytes, ml_library=ml_library, nn_type=nn_type)
    return (
        model_predict(
            ml_model_file=ml_model_as_bytes,
            ml_library=ml_library,
            image_as_array=image_as_array,
            custom_objects=custom_objects,
            threshold=threshold,
        )
        .flatten()
        .tolist()
    )
