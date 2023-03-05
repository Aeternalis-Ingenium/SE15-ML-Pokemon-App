import enum


class MLModelFileExtension(str, enum.Enum):
    HDF5_1 = "h5"
    HDF5_2 = "hdf5"
    PICKLE = "pkl"


class PokemonImageFileExtension(str, enum.Enum):
    PNG = "png"
    JPG = "jpg"
