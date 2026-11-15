import yt_dlp


# Descargar en MP3
def descargarMP3(listaURL):
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
        "outtmpl": "%(channel)s - %(title)s.%(ext)s",
    }

    for url in listaURL:
        with yt_dlp.YoutubeDL(configuracion) as ydl:
            ydl.download([url])

    print("Descarga Finalizada")


# Descargar en MP4
def descargarMP4(listaURL):
    print("Iniciando descarga del mp4...")
    configuracion = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "restrictfilenames": True,
        "merge_output_format": "mp4",
        "outtmpl": "%(channel)s - %(title)s.%(ext)s",
    }

    for url in listaURL:
        with yt_dlp.YoutubeDL(configuracion) as ydl:
            ydl.download([url])

    print("Descarga Finalizada")


# Verificar url
def verificarURL(url):
    print("Verificando URL...")
    configuracion = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": True,
        "skip_download": True,
    }

    try:
        with yt_dlp.YoutubeDL(configuracion) as ydl:
            info = ydl.extract_info(url, download=False)
            if info:
                print("URL Valida")
                print("Titulo:", info.get("title"))
                print("Canal:", info.get("channel"))
                return True
            else:
                return False
    except yt_dlp.utils.DownloadError:
        print("La URL no es valida, no existe o es inaccesible.")


def main():
    listaURL = []

    print("=== GESTOR DE DESCARGAS YOUTUBE ===")
    print("Instrucciones: Ingrese las URL una por una.")
    print("Escriba '0' cuando termine para continuar con el menu de descarga.\n")

    while True:
        url = input("Ingresa la URL (o '0' para terminar): ")

        if not url:
            print("URL vacia. Intente de nuevo.\n")
        elif url == "0":
            break
        elif verificarURL(url):
            listaURL.append(url)
            print("URL agregada correctamente.\n")
        else:
            print()

    if not listaURL:
        print("No se ingresaron URLs. Cerrando programa...")
    else:
        try:
            while True:
                print("\n" + "=" * 30)
                print("       MENU DE FORMATOS       ")
                print("=" * 30)
                print("1. Descargar en MP3 (Audio)")
                print("2. Descargar en MP4 (Video)")
                print("3. Salir")
                print("-" * 30)

                try:
                    opcion = int(input("Seleccione una opcion (1-3): "))
                except ValueError:
                    print("Por favor, ingrese un numero valido.")
                    continue

                match opcion:
                    case 1:
                        descargarMP3(listaURL)
                        break
                    case 2:
                        descargarMP4(listaURL)
                        break
                    case 3:
                        print("Saliendo sin descargar...")
                        break
                    case _:
                        print("Opcion no valida. Intente de nuevo.")

        except Exception as e:
            print(f"Ocurrio un error durante la descarga: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario. Cerrando...")
    except Exception as e:
        print(f"Ocurrio un error durante la ejecucion del programa: {e}")
