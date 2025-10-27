def listado():
    print()


def conteo():
    nombre_archivo = input("ingrese el nombre del archivo a procesar (ingresar el nombre y su extensión): ")
    print ("Contando número de palabras y caracteres...\n...")
    with open(".\\src\\Reto_unidad_5\\Archivos_reto5\\" + nombre_archivo , "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    num_caracteres = len(contenido)
    palabras = contenido.split()
    num_palabras = len(palabras)
    print(f"Número de caracteres: {num_caracteres}")
    print(f"Número de palabras: {num_palabras}")


def reemplazo():
    print()

def histograma():
    print()

def vista_previa():
    print()

def estadisticas():
    print()

def grafica():        
    print()

def OP1():
    print ("Estos son los archivos que tiene disponible para trabajar:")
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
