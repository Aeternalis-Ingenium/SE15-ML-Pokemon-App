import pathlib

import decouple


class Directory:
    def __init__(self):
        self._ROOT_DIR: pathlib.Path = pathlib.Path(__file__).resolve().parent.parent.parent
        self._ASSET_DIR: pathlib.Path = self._ROOT_DIR / pathlib.Path(decouple.config("ASSET_DIR_NAME", cast=str))  # type: ignore
        self.CSV_DIR: pathlib.Path = self._ASSET_DIR / pathlib.Path(decouple.config("CSV_DIR_NAME", cast=str))  # type: ignore
        self.ELEMENT_TYPE_DIR: pathlib.Path = self._ASSET_DIR / pathlib.Path(decouple.config("ELEMENT_TYPE_DIR_NAME", cast=str))  # type: ignore
        self.ML_MODEL_DIR: pathlib.Path = self._ASSET_DIR / pathlib.Path(decouple.config("ML_MODEL_DIR_NAME", cast=str))  # type: ignore


project_dir = Directory()
