import os
from datetime import datetime
from PIL import Image, UnidentifiedImageError

# Ruta al directorio con las fotos y videos
directorio = "D:/media/DCIM/Concerts/taylor"

# Nombre personalizado
nombre_personalizado = "TaylorSwift"

# Extensiones soportadas
EXTENSIONES_IMAGEN = {'.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif', '.heic', '.webp'}
EXTENSIONES_VIDEO = {'.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.m4v', '.3gp'}

# Función para obtener la fecha de una imagen desde EXIF
def obtener_fecha_tomada(path):
    try:
        imagen = Image.open(path)
        exif_data = imagen._getexif()
        if exif_data and 36867 in exif_data:  # Tag DateTimeOriginal
            fecha_tomada = exif_data[36867]
            return datetime.strptime(fecha_tomada, '%Y:%m:%d %H:%M:%S').strftime('%Y-%m-%d_%H%M%S')
        return None
    except UnidentifiedImageError:
        print(f"[ERROR] El archivo no es una imagen válida: {path}")
        return None
    except Exception as e:
        print(f"[ERROR] No se pudo obtener la fecha EXIF de {path}: {e}")
        return None

# Función para generar un nombre único si el archivo ya existe
def generar_nombre_unico(ruta_nueva):
    base, extension = os.path.splitext(ruta_nueva)
    contador = 1
    while os.path.exists(ruta_nueva):
        ruta_nueva = f"{base}_{contador}{extension}"
        contador += 1
    return ruta_nueva

# Contador inicial para números secuenciales
contador = 1

for nombre_archivo in os.listdir(directorio):
    extension = os.path.splitext(nombre_archivo)[1].lower()
    ruta_completa = os.path.join(directorio, nombre_archivo)

    # Solo procesar imágenes o videos
    if extension in EXTENSIONES_IMAGEN or extension in EXTENSIONES_VIDEO:
        try:
            if extension in EXTENSIONES_IMAGEN:
                fecha_tomada = obtener_fecha_tomada(ruta_completa)
            else:
                fecha_tomada = None  # No hay EXIF en videos

            if not fecha_tomada:
                fecha_tomada = datetime.fromtimestamp(os.path.getmtime(ruta_completa)).strftime('%Y-%m-%d_%H%M%S')

            numero_secuencial = str(contador).zfill(4)
            nuevo_nombre = f"{fecha_tomada}_{nombre_personalizado}_{numero_secuencial}{extension}"
            ruta_nueva = os.path.join(directorio, nuevo_nombre)

            # Evitar sobrescribir archivos existentes
            ruta_nueva = generar_nombre_unico(ruta_nueva)

            os.rename(ruta_completa, ruta_nueva)
            print(f"[OK] {nombre_archivo} -> {nuevo_nombre}")
            contador += 1

        except Exception as e:
            print(f"[ERROR] No se pudo renombrar {nombre_archivo}: {e}")
    else:
        print(f"[X] Saltando archivo no compatible: {nombre_archivo}")

print("Renombrado completado.")
