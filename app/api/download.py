from fastapi import APIRouter
from app.models.video import VideoRequest
from app.services.download_service import processar_download

router = APIRouter()

@router.post("/download")
def download(video: VideoRequest):

    resultado = processar_download(video.url)

    return resultado
