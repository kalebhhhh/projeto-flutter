def validar_url(url: str):
    return "instagram.com" in url

def obter_plataforma(url: str):
    if "instagram.com" in url:
        return "instagram"
    return "desconhecido"

def eh_instagram(url: str):
    if "instagram.com" in url:
        return True
    return False