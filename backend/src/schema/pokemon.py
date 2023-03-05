from src.schema.base import BaseSchemaModel


class UploadPokemonInResponse(BaseSchemaModel):
    image_file_extension: str | None
    is_verified_image: bool
