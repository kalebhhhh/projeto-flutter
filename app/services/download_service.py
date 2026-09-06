from app.services.video_service import eh_instagram

def processar_download(url: str):

    if not eh_instagram(url):
        return {
            "status":"erro",
            "mensagem":"URL não é válida!!"
        }
    return{
        "status":"sucesso",
        "mensagem":"URL Válida",
        "url": url
    }