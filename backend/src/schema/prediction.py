from src.schema.base import BaseSchemaModel


class PredictionInResponse(BaseSchemaModel):
    prediction: list
    predicted_element_type_1: str
    predicted_element_Type_2: str | None
    actual_element_type_1: str
    actual_element_Type_2: str | None
    is_prediction_correct: bool
