#Abrir el archivo y definir el modo
lectura = open("./src/archivos/texto1.txt", "r")
#leer el archivo
"""
for i in range (5):
    seleccion1 = lectura.readline()
print(seleccion1)

for seleccion1 in lectura:
    print(seleccion1[0])
"""
seleccion1 = lectura.readlines()
print(seleccion1)
#cerrar
lectura.close()

#EOF significa end of file