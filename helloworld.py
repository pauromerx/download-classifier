import os
import shutil

# Localizamos la carpeta a organizar
download_folder = "E:/adrim/Documents/Code/Carpeta a organizar"

# Creamos una lista que guarde el nombre y la ext de todos los archivos de la carpeta
list = os.listdir(download_folder)
print(list)

# Para cada posición de la lista separamos nombre y extensión
# PROBLEMA: Si hay un punto intermedio en el nombre?
# PROBLEMA: Hay que poner name y ext como listas
"""
for file in list:
    name, ext = file.split(".")
print(name, ext)
"""

#TIPOS DE ARCHIVOS

TEXTO = ["txt", "doc", "docx", "pdf"]
IMAGENES = ["jpg", "gif", "bmp", "png"]
VIDEOS = ["avi", "mp4", "mpeg", "mwv"]
EJECUCIONES_DE_SISTEMA = ["exe", "bat", "dll", "sys"]
AUDIOS = ["mp3", "wav", "wma"]
COMPRIMIDOS = ["zip", "rar", "tar"]
IMAGENES_DE_DISCO = ["iso", "mds", "img"]

##################
