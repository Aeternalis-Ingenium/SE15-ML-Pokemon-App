import numpy as np
import pandas as pd

from src.config.settings import settings


def get_pokemon_table():
    df = pd.read_csv(filepath_or_buffer=settings.POKEMON_CSV)
    df = df.replace(to_replace=np.NaN, value=None)
    df["Type1"] = df["Type1"].apply(lambda value: value.lower() if value != None else None)  # type: ignore
    df["Type2"] = df["Type2"].apply(lambda value: value.lower() if value != None else None)  # type: ignore
    return df


def get_verified_pokemon_name(df: pd.DataFrame, pokemon_name: str) -> str:
    pokemon_table = df[df["Name"] == pokemon_name.lower()]
    if not pokemon_table["Name"].any():
        raise Exception(f"Pokemon name `{pokemon_name.lower()}` is not listed. Re-check your Pokemon name!")
    return pokemon_table.values[0].tolist()[0]
