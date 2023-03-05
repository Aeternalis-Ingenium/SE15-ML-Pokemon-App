import fastapi

from src.api.routes.inference import router as inference_router
from src.api.routes.upload import router as upload_router

router = fastapi.APIRouter(
    prefix="/v1",
)

router.include_router(router=inference_router)
router.include_router(router=upload_router)
