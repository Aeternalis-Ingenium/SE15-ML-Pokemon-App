from src.utility.enum.element_types import PokemonElementTypes
from src.utility.verification.pokemon import get_pokemon_table, get_verified_pokemon_name


async def interpret_prediction(prediction: list, pokemon_name) -> tuple[str, str, str | None, str, str | None, bool]:
    pokemon_table = get_pokemon_table()
    verified_pokemon_name = get_verified_pokemon_name(df=pokemon_table, pokemon_name=pokemon_name)
    pokemon = pokemon_table[pokemon_table["Name"] == verified_pokemon_name]
    predicted_element_types = list()
    actual_element_types = pokemon.values[0].tolist()[1:]

    for idx in range(len(prediction)):
        for element_type in PokemonElementTypes:
            if prediction[idx] == True:
                if idx == element_type.value:
                    predicted_element_types.append(str(element_type.name).lower())

    if len(predicted_element_types) == 0:
        raise Exception(f"Your ML model didn't have any True prediction! Try to adjust the `prediction threshold`")
    elif len(predicted_element_types) == 1:
        predicted_element_types.append(None)  # type: ignore

    is_prediction_correct = predicted_element_types == actual_element_types

    return (
        verified_pokemon_name,
        predicted_element_types[0],
        predicted_element_types[-1],
        actual_element_types[0],
        actual_element_types[-1],
        is_prediction_correct,
    )
