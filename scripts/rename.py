import os
from datetime import datetime
from PIL import Image

# Ruta al directorio con las fotos
directorio = "dir"

# Nombre personalizado (como "TaylorSwift" en tu ejemplo)
nombre_personalizado = "TaylorSwift"

# Función para obtener la fecha en que se tomó la foto
def obtener_fecha_tomada(path):
    try:
        # Abre la imagen usando Pillow
        imagen = Image.open(path)
        # Obtén los metadatos EXIF
        exif_data = imagen._getexif()

        # El tag 36867 es 'DateTimeOriginal' en EXIF
        if exif_data and 36867 in exif_data:
            fecha_tomada = exif_data[36867]
            # Formato de fecha: 'YYYY:MM:DD HH:MM:SS', convertir a 'YYYY-MM-DD_HHMMSS'
            fecha_formateada = datetime.strptime(fecha_tomada, '%Y:%m:%d %H:%M:%S').strftime('%Y-%m-%d_%H%M%S')
            return fecha_formateada
        else:
            return None
    except Exception as e:
        print(f"No se pudo obtener la fecha para {path}: {e}")
        return None

# Contador inicial para los números secuenciales
contador = 1

# Renombrar cada archivo en el directorio
for nombre_archivo in os.listdir(directorio):
    # Obtener la extensión del archivo
    extension = os.path.splitext(nombre_archivo)[1].lower()

    # Filtrar solo archivos de imagen y video (puedes agregar más extensiones si es necesario)
    if extension in ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif', '.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.m4v'):
        ruta_completa = os.path.join(directorio, nombre_archivo)

        # Obtener la fecha en que se tomó la foto o se modificó el video
        fecha_tomada = obtener_fecha_tomada(ruta_completa) if extension in ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif') else None
        
        # Si la fecha no se puede obtener de EXIF, usa la fecha de modificación del archivo
        if not fecha_tomada:
            fecha_tomada = datetime.fromtimestamp(os.path.getmtime(ruta_completa)).strftime('%Y-%m-%d_%H%M%S')

        # Crear el número secuencial de 4 dígitos
        numero_secuencial = str(contador).zfill(4)

        # Crear el nuevo nombre de archivo con el formato requerido y la misma extensión
        nuevo_nombre = f"{fecha_tomada}_{nombre_personalizado}_{numero_secuencial}{extension}"
        ruta_nueva = os.path.join(directorio, nuevo_nombre)

        # Renombrar el archivo
        os.rename(ruta_completa, ruta_nueva)

        # Incrementar el contador para el siguiente archivo
        contador += 1
    else:
        # Si el archivo no es una imagen o video, simplemente salta al siguiente archivo
        print(f"[X] Saltando archivo no compatible: {nombre_archivo}")

print("Renombrado completado.")
