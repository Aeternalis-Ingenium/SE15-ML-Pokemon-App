from src.schema.base import BaseSchemaModel


class UploadMLModelInResponse(BaseSchemaModel):
    model_file_extension: str | None
    is_verified_model_file: bool
