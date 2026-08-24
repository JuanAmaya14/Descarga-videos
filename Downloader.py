import yt_dlp


# Descargar en MP3
def descargarMP3(URL):
    print("Iniciando descarga del mp3...")
    configuracion = {
        "format": "bestaudio/best",
        "restrictfilenames": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "outtmpl": "%(title)s.%(ext)s",
    }

    with yt_dlp.YoutubeDL(configuracion) as ydl:
        ydl.download([URL])

    print("Descarga Finalizada")


# Descargar en MP4
def descargarMP4(URL):
    print("Iniciando descarga del mp4...")
    configuracion = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "restrictfilenames": True,
        "merge_output_format": "mp4",
        "outtmpl": "%(title)s.%(ext)s",
    }

    with yt_dlp.YoutubeDL(configuracion) as ydl:
        ydl.download([URL])

    print("Descarga Finalizada")


# Verificar url
def verificarURL(URL):
    print("Verificando URL...")
    configuracion = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": True,
        "skip_download": True,
    }

    try:
        with yt_dlp.YoutubeDL(configuracion) as ydl:
            info = ydl.extract_info(URL, download=False)
            if info:
                print("URL Valido")
                print('Titulo:', info.get('title'))
                return True
    except yt_dlp.utils.DownloadError:
        print("La URL no es valida, no existe o es inaccesible.")


def main():
    URL = input("Ingresa la URL: ")

    if not URL:
        print("ERROR: La URL esta vacia.")
    else:
        if verificarURL(URL):
            try:
                # Menu
                while True:
                    menu = """Escoge en que formato lo quieres descargar:
1. mp3
2. mp4
> """

                    opcion = int(input(menu))

                    match opcion:
                        case 1:
                            descargarMP3(URL)
                            break
                        case 2:
                            descargarMP4(URL)
                            break
                        case _:
                            print("Opcion no valida")

            except Exception as e:
                print(f"Ocurrio un error durante la descarga: {e}")


main()
