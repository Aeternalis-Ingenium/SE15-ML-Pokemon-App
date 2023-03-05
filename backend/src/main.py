import fastapi
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles as FastAPIStaticFiles

from src.api.endpoints import router as endpoint_router
from src.config.settings import settings


def initialize_application() -> fastapi.FastAPI:
    app = fastapi.FastAPI(**settings.set_backend_app_attributes)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=settings.IS_ALLOWED_CREDENTIALS,
        allow_methods=settings.ALLOWED_METHODS,
        allow_headers=settings.ALLOWED_HEADERS,
    )
    # Static URL: http:/0.0.0.0:8001/assets/
    app.mount(path="/assets", app=FastAPIStaticFiles(directory="assets"), name="assets")
    app.include_router(router=endpoint_router, prefix=settings.API_PREFIX)
    return app


app: fastapi.FastAPI = initialize_application()

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.DEBUG,
        workers=settings.SERVER_WORKERS,
        log_level=settings.LOGGING_LEVEL,
    )
