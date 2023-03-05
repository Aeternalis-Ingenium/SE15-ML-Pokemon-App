import logging
import pathlib
from functools import lru_cache

import decouple
import pydantic

from src.config.directory import Directory, project_dir


class Settings(pydantic.BaseSettings):
    TITLE: str = "ML Ex-Project App "
    VERSION: str = decouple.config("API_VERSION", cast=str)  # type: ignore
    TIMEZONE: str = "UTC"
    DESCRIPTION: str = f"Web app for testing stuents' ML Model --- Version {VERSION}"
    DEBUG: bool = False

    SERVER_HOST: str = decouple.config("BACKEND_SERVER_HOST", cast=str)  # type: ignore
    SERVER_PORT: int = decouple.config("BACKEND_SERVER_PORT", cast=int)  # type: ignore
    SERVER_WORKERS: int = decouple.config("BACKEND_SERVER_WORKERS", cast=int)  # type: ignore
    API_PREFIX: str = "/api"
    DOCS_URL: str = "/docs"
    OPENAPI_URL: str = "/openapi.json"
    REDOC_URL: str = "/redoc"
    OPENAPI_PREFIX: str = ""

    API_KEY: str = decouple.config("API_KEY", cast=str)  # type: ignore

    IS_ALLOWED_CREDENTIALS: bool = decouple.config("IS_ALLOWED_CREDENTIALS", cast=bool)  # type: ignore
    ALLOWED_ORIGINS: list[str] = [
        decouple.config("CLIENT_ORIGIN_LOCALHOST", cast=str),  # type: ignore
        decouple.config("CLIENT_ORIGIN_DOCKER", cast=str),  # type: ignore
    ]
    ALLOWED_METHODS: list[str] = [decouple.config("CLIENT_METHOD")]  # type: ignore
    ALLOWED_HEADERS: list[str] = [decouple.config("CLIENT_HEADER")]  # type: ignore

    LOGGING_LEVEL: int = logging.INFO
    LOGGERS: tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")
    POKEMON_CSV: pathlib.Path = project_dir.CSV_DIR / pathlib.Path(decouple.config("CSV_FILE_NAME", cast=str))  # type: ignore
    ML_LOCAL_MODEL: pathlib.Path = project_dir.ML_MODEL_DIR / pathlib.Path(decouple.config("ML_LOCAL_MODEL_NAME", cast=str))  # type: ignore

    class Config(pydantic.BaseConfig):
        case_sensitive: bool = True
        env_file: str = f"{str(project_dir._ROOT_DIR)}/.env"
        validate_assignment: bool = True

    @property
    def set_backend_app_attributes(self) -> dict[str, str | bool | None]:
        """
        Set all `FastAPI` instance attributes with the custom values defined in `Settings`.
        """
        return {
            "title": self.TITLE,
            "version": self.VERSION,
            "debug": self.DEBUG,
            "description": self.DESCRIPTION,
            "docs_url": self.DOCS_URL,
            "openapi_url": self.OPENAPI_URL,
            "redoc_url": self.REDOC_URL,
            "openapi_prefix": self.OPENAPI_PREFIX,
            "api_prefix": self.API_PREFIX,
        }


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
