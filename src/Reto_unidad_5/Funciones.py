def listado():
    

def conteo():
    print ("Contando número de palabras y caracteres...\n...")
    

def reemplazo():


def histograma():


def vista_previa():


def estadisticas():


def grafica():        


def OP1():
    print ("Estos son los archivos que tiene disponible para trabajar:")
    listado()


def OP2():
    opc = int(input("(1) Contar número de archivos.\n(2) Reemplazar palabras.\n(3) Histograma de ocurrencias.\nIngrese la opción: "))
        match (opc):
            case 1:
                print ("Contar número de archivos.")
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
