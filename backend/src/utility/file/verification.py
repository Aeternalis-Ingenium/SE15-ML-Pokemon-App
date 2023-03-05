from src.utility.enum.file import MLModelFileExtension, PokemonImageFileExtension


def verify_file_extension(file_extension: str):
    match file_extension:
        case PokemonImageFileExtension.JPG:
            pass
        case PokemonImageFileExtension.PNG:
            pass
        case MLModelFileExtension.HDF5_1:
            pass
        case MLModelFileExtension.HDF5_2:
            pass
        case MLModelFileExtension.PICKLE:
            pass
        case _:
            return (None, False)
    return (file_extension, True)
