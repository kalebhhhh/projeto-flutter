from fastapi import APIRouter;
from app.services.video_service import validar_url
from app.services.video_service import obter_plataforma
from app.services.video_service import eh_instagram

router = APIRouter()

@router.get("/health")
def health():
    return {
        "status": "rota health"
    }

@router.get("/version")
def version(): 
    return {
        "status":"rota version"
    }

@router.get("/saudar/{nome}")
def saudar(nome: str):
    return {
        "mensagem": f"Olá {nome}!"
    }

@router.get("/calcular/{valor}")
def calcular(valor: int):
    return{
        "número": valor,
        "dobro": valor*2
    }

@router.get("/plataforma")
def plataforma():
    url = "https://instagram.com/reel/123"
    resultado = obter_plataforma(url)
    return{
        "url": url,
        "plataforma": resultado
    }

@router.get("/validar")
def validar(url: str):

    resultado = eh_instagram(url)

    return {
        "url_recebida": url,
        "resultado": resultado
    }