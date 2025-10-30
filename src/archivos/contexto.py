location = "C:\\Users\\B09S202est\\Desktop\\Archivos"
nombre_archivo = "./src/archivos/texto1.txt"
with open(nombre_archivo, "r", encoding="utf-8") as archivo:# Hacer operaciones con el archivo
    lista1 = archivo.readlines()
# El archivo se cierra automáticamente al salir del bloque with

for c in lista1:
    print(c)
