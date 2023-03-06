import io

import fastapi
import h5py

from src.schema.prediction import PredictionInResponse
from src.utility.enum.ml import MLModelLibrary
from src.utility.pipeline.inference import inference_pipeline
from src.utility.pipeline.result import interpret_prediction

router = fastapi.APIRouter(prefix="/se15", tags=["inference"])


@router.post(
    path="/inference/predict-element-types",
    response_model=PredictionInResponse,
    status_code=fastapi.status.HTTP_200_OK,
)
async def predict_pokemon(
    pokemon_image_file: fastapi.UploadFile,
    ml_model_file: fastapi.UploadFile,
    pokemon_name: str = fastapi.Body(..., embed=True),
    ml_library: str = fastapi.Body(..., embed=True),
    nn_type: str | None = fastapi.Body(..., embed=True),
    nn_prediction_threshold: float | None = fastapi.Body(..., embed=True),
):
    data: dict = dict()
    pokemon_immage_as_bytes = await pokemon_image_file.read()
    ml_model_as_bytes = await ml_model_file.read()
    prediction = None
    try:
        if ml_library == MLModelLibrary.TF:
            h5_file = h5py.File(name=io.BytesIO(initial_bytes=ml_model_as_bytes))
            prediction = await inference_pipeline(
                pokemon_image_as_bytes=pokemon_immage_as_bytes,
                ml_model_as_bytes=h5_file,
                threshold=nn_prediction_threshold,
                ml_library=ml_library,
                nn_type=nn_type,
            )
        elif ml_library == MLModelLibrary.SKLEARN:
            prediction = await inference_pipeline(
                pokemon_image_as_bytes=pokemon_immage_as_bytes,
                ml_model_as_bytes=ml_model_as_bytes,
                threshold=nn_prediction_threshold,
                ml_library=ml_library,
                nn_type=nn_type,
            )
    except Exception:
        raise fastapi.exceptions.HTTPException(
            status_code=fastapi.status.HTTP_400_BAD_REQUEST,
            detail=f"Your ML model doesn't predict any True value. Try to change your prediction value or use other model!",
        )
    (
        data["verified_pokemon_name"],
        data["predicted_element_type_1"],
        data["predicted_element_Type_2"],
        data["actual_element_type_1"],
        data["actual_element_Type_2"],
        data["is_prediction_correct"],
    ) = await interpret_prediction(
        prediction=prediction, pokemon_name=pokemon_name  # type: ignore
    )
    return PredictionInResponse(**data)
