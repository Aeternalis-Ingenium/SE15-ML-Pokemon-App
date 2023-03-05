import fastapi

from src.schema.ml_model import UploadMLModelInResponse
from src.schema.pokemon import UploadPokemonInResponse
from src.utility.file.verification import verify_file_extension

router = fastapi.APIRouter(prefix="/upload", tags=["upload"])


@router.post(path="/pokemon", response_model=UploadPokemonInResponse, status_code=fastapi.status.HTTP_200_OK)
async def upload_pokemon_image(
    file: fastapi.UploadFile,
) -> UploadPokemonInResponse:
    data: dict = dict()
    image_file_extension = str(file.filename).split(".")[-1]
    data["image_file_extension"], data["is_verified_image"] = verify_file_extension(
        file_extension=image_file_extension
    )
    return UploadPokemonInResponse(**data)


@router.post(path="/ml-model", response_model=UploadMLModelInResponse, status_code=fastapi.status.HTTP_200_OK)
async def upload_ml_model(
    file: fastapi.UploadFile,
) -> UploadMLModelInResponse:
    data: dict = dict()
    model_file_extension = str(file.filename).split(".")[-1]
    data["model_file_extension"], data["is_verified_model_file"] = verify_file_extension(
        file_extension=model_file_extension
    )
    return UploadMLModelInResponse(**data)
