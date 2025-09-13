# 🛸 Abduction

```
     🛸
    /   \
   /_____\
  |  ◉ ◉  |
  |   ∩   |
   \  ∨  /
    \___/
```

Un descargador de videos de TikTok simple y eficiente.

## 📋 Descripción

Abduction es una herramienta de línea de comandos que permite descargar múltiples videos de TikTok desde un archivo de enlaces. Los videos se organizan automáticamente y se generan logs detallados para seguimiento.

## 🚀 Instalación

### Prerrequisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Configuración con Virtual Environment (Recomendado)

Es **altamente recomendado** usar un entorno virtual para evitar conflictos de dependencias:

```bash
# 1. Crear un entorno virtual
python -m venv venv

# 2. Activar el entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

## 📖 Uso

```bash
python abduction.py <ruta_archivo_links>
```

**Importante:** Si la ruta contiene espacios, usa comillas dobles:

```bash
python abduction.py "ruta con espacios/links.txt"
```

### Ejemplos

```bash
# Ruta relativa simple
python abduction.py links.txt

# Ruta absoluta
python abduction.py C:\Users\usuario\Documents\links.txt

# Ruta con espacios (usar comillas dobles)
python abduction.py "C:\Users\mi usuario\Mis Documentos\links.txt"
```

### Formato del archivo de enlaces

Crea un archivo de texto con los enlaces de TikTok, uno por línea:

```
https://www.tiktok.com/@usuario/video/1234567890
https://www.tiktok.com/@usuario/video/9876543210
https://www.tiktok.com/@usuario/video/5555555555
```

## 📁 Estructura de archivos

```
abduction/
├── abduction.py          # Script principal
├── requirements.txt      # Dependencias
├── links.txt            # Archivo con enlaces (ejemplo)
├── videos_tiktok/       # Videos descargados
└── logs/               # Archivos de log
    ├── descargas_ok_*.log     # Enlaces exitosos
    └── descargas_error_*.log  # Enlaces con errores
```

## ⚙️ Características

- ✅ Descarga múltiples videos de TikTok
- 📁 Organización automática de archivos
- 📊 Logs detallados de descargas exitosas y errores
- 🔧 Parámetro personalizable para archivo de enlaces
- 🛡️ Validación de argumentos y archivos

## 🔧 Dependencias

- `yt-dlp`: Librería para descargar videos

## 💡 Consejos

- Usa siempre un entorno virtual para mantener las dependencias organizadas
- Los logs se generan con timestamp para evitar sobreescritura
- Solo se descargan enlaces que contengan "/video/" en la URL
- Los videos se guardan en formato MP4

## 🚫 Desactivar entorno virtual

Cuando termines de usar la herramienta:

```bash
deactivate
```

---

*¡Felices descargas! 🛸*