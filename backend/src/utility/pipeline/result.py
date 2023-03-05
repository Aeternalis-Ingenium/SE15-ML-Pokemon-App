import numpy as np
import pandas as pd

from src.config.settings import settings
from src.utility.enum.element_types import PokemonElementTypes


def get_pokemon_table():
    df = pd.read_csv(filepath_or_buffer=settings.POKEMON_CSV)
    df = df.replace(to_replace=np.NaN, value=None)
    df["Type1"] = df["Type1"].apply(lambda value: value.lower() if value != None else None)  # type: ignore
    df["Type2"] = df["Type2"].apply(lambda value: value.lower() if value != None else None)  # type: ignore
    return df


async def interpret_prediction(prediction: list, pokemon_name) -> tuple[str, str | None, str, str | None, bool]:
    pokemon_table = get_pokemon_table()
    pokemon = pokemon_table[pokemon_table["Name"] == pokemon_name.lower()]
    predicted_element_types = list()
    actual_element_types = pokemon.values[0].tolist()[1:]

    for idx in range(len(prediction)):
        for element_type in PokemonElementTypes:
            if prediction[idx] == True:
                if idx == element_type.value:
                    predicted_element_types.append(str(element_type.name).lower())

    if len(predicted_element_types) == 1:
        predicted_element_types.append(None)  # type: ignore

    is_prediction_correct = predicted_element_types == actual_element_types

    return (
        predicted_element_types[0],
        predicted_element_types[-1],
        actual_element_types[0],
        actual_element_types[-1],
        is_prediction_correct,
    )
