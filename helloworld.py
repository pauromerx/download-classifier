import os
import shutil

#TIPOS DE ARCHIVOS

TEXTO = ["txt", "doc", "docx", "pdf"]
IMAGENES = ["jpg", "gif", "bmp", "png"]
VIDEOS = ["avi", "mp4", "mpeg", "mwv"]
EJECUCIONES_DE_SISTEMA = ["exe", "bat", "dll", "sys"]
AUDIOS = ["mp3", "wav", "wma"]
COMPRIMIDOS = ["zip", "rar", "tar"]
IMAGENES_DE_DISCO = ["iso", "mds", "img"]

##################

# Localizamos la carpeta a organizar
download_folder = "E:/adrim/Documents/Code/Carpeta a organizar"

# Creamos una lista que guarde el nombre y la ext de todos los archivos de la carpeta
list = os.listdir(download_folder)
print(list)

# Para cada posición de la lista separamos nombre y extensión y lo guardamos en unas variables que luego
# las vamos pasando a dos listas.


name_list = []
ext_list = []

for file in list:
    name, ext = file.split(".")
    name_list.append(name)
    ext_list.append(ext)
print("Nombres de los archivos: " + str(name_list))
print("Extensiones de los archivos: " + str(ext_list))