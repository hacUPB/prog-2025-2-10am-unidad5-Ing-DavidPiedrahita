import csv
from Funciones import *

def main():
    print ("Bienvenido, este menú le permitirá realizar las siguientes tareas:")
    while True:
        opcion = int(input("(1) Lista de Archivos.\n(2) Procesar un archivo de texto (.txt).\n(3) Procesar un archivo separado por comas (.csv).\n(4) Salir\nIngrese la opción: "))
        match (opcion):
            case 1:
                print ("Opción seleccionada: Lista de Archivos.")
                OP1()
            case 2:
                print ("Opción seleccionada: Procesar un archivo de texto.")
                OP2()
            case 3:
                print ("Opción seleccionada: Procesar un archivo separado por comas.")                
                OP3()
            case 4:
                print ("Saliendo...")
                break
            case _:  
                print ("Opción no válida.")              

if __name__ == "__main__":
    main()