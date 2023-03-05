import enum


class MLModelLibrary(str, enum.Enum):
    TF = "tensorflow"
    SKLEARN = "scikit-learn"


class NNArchitecture(str, enum.Enum):
    ANN = "ANN"
    CNN = "CNN"
