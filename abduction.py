import yt_dlp
import os
import sys
from datetime import datetime

def main():
    # Verificar argumentos
    if len(sys.argv) != 2:
        print("❌ Uso: python abduction.py <ruta_archivo_links>")
        print("   Ejemplo: python abduction.py links.txt")
        sys.exit(1)
    
    RUTA_ARCHIVO = sys.argv[1]
    
    # Verificar que el archivo existe
    if not os.path.exists(RUTA_ARCHIVO):
        print(f"❌ Error: El archivo '{RUTA_ARCHIVO}' no existe.")
        sys.exit(1)
    
    # Crear carpetas necesarias
    CARPETA_DESCARGA = "videos_tiktok"
    CARPETA_LOGS = "logs"
    os.makedirs(CARPETA_DESCARGA, exist_ok=True)
    os.makedirs(CARPETA_LOGS, exist_ok=True)
    
    # Archivos de log en carpeta logs
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_exitos = os.path.join(CARPETA_LOGS, f"descargas_ok_{timestamp}.log")
    log_errores = os.path.join(CARPETA_LOGS, f"descargas_error_{timestamp}.log")
    
    # Leer y filtrar enlaces (solo videos)
    with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
        links = [line.strip() for line in f if line.strip() and "/video/" in line]
    
    print(f"🎯 Total de videos a descargar: {len(links)}")
    
    # Configuración de yt_dlp
    opciones = {
        'outtmpl': os.path.join(CARPETA_DESCARGA, '%(title).70s.%(ext)s'),
        'format': 'mp4',
        'quiet': False,
        'noplaylist': True
    }
    
    # Descarga con logging
    with yt_dlp.YoutubeDL(opciones) as ydl:
        for link in links:
            try:
                print(f"📥 Descargando: {link}")
                ydl.download([link])
                with open(log_exitos, "a", encoding="utf-8") as log_ok:
                    log_ok.write(link + "\n")
            except Exception as e:
                print(f"❌ Error con {link}: {e}")
                with open(log_errores, "a", encoding="utf-8") as log_fail:
                    log_fail.write(f"{link} | {e}\n")
    
    print("✅ Proceso completado.")
    print(f"✔️ Log de éxitos: {log_exitos}")
    print(f"❗ Log de errores: {log_errores}")

if __name__ == "__main__":
    main()
