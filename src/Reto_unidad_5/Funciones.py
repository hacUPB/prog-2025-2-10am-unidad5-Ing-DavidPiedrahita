import os
import csv
import matplotlib.pyplot as plt
def listado():
    ruta = input("Ingrese la ruta donde desea buscar los archivos:\n")
    if ruta == "":
        ruta = os.getcwd()
    archivos = os.listdir(ruta)
    print("\nArchivos encontrados:")
    for archivo in archivos:
        print(f"- {archivo}")


def conteo():
    nombre_archivo = input("Ingrese el nombre del archivo de texto: ")
    ruta = "./src/Reto_unidad_5/Archivos_reto5/" + nombre_archivo
    print ("Contando número de palabras y caracteres...\n...")
    with open(ruta, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    num_caracteres = len(contenido)
    palabras = contenido.split()
    num_palabras = len(palabras)
    print(f"Número de caracteres: {num_caracteres}")
    print(f"Número de palabras: {num_palabras}")


def reemplazo():
    nombre_archivo = input("Ingrese el nombre del archivo de texto: ")
    palabra_original = input("Ingrese la palabra que desea reemplazar: ")
    palabra_nueva = input("Ingrese la nueva palabra: ")
    ruta = "./src/Reto_unidad_5/Archivos_reto5/" + nombre_archivo
    with open(ruta, "r", encoding="utf-8") as archivo:
         contenido = archivo.read()
    nuevo_contenido = contenido.replace(palabra_original, palabra_nueva)
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write(nuevo_contenido)
    print("Reemplazo realizado con éxito.")


def histograma():
    nombre_archivo = input("Ingrese el nombre del archivo de texto: ")
    ruta = "./src/Reto_unidad_5/Archivos_reto5/" + nombre_archivo
    with open(ruta, "r", encoding="utf-8") as archivo:
        contenido = archivo.read().lower()
#    vocales = ["a","e","i","o","u"]
    vocales = []
    for i in contenido: 
        if i in "aeiou":
            vocales.append(i)
    plt.hist(vocales, bins=100, edgecolor='black', color='skyblue')
    plt.title("Histograma de ocurrencias de vocales")
    plt.xlabel("Vocales")
    plt.ylabel("Frecuencia")
    plt.show()


def vista_previa():
    print()

def estadisticas():
    print()

def grafica():        
    print()

def OP1():
    print ("A continuación podrá observar los archivos que tiene disponible para trabajar:")
    listado()


def OP2():
    opc = int(input("(1) Contar número de palabras y caracteres.\n(2) Reemplazar palabras.\n(3) Histograma de ocurrencias.\nIngrese la opción: "))
    match (opc):
            case 1:
                print ("Conteo de número de palabras y caracteres.")
                conteo()
            case 2:
                print ("Reemplazar palabras.")
                reemplazo()
            case 3:
                print ("Histograma de ocurrencias.")                
                histograma()
            case _:  
                print ("Opción no válida.")


def OP3():
    opt = int(input("(1) Vista previa del archivo.\n(2) Calcular estadísticas.\n(3) Graficar una columna completa con los datos.\nIngrese la opción: "))
    match (opt):
            case 1:
                print ("Vista previa.")
                vista_previa()
            case 2:
                print ("Estadísticas.")
                estadisticas()
            case 3:
                print ("Gráfica.")                
                grafica()
            case _:  
                print ("Opción no válida.")
