import csv

with open('C:\\Users\\B09S202est\\Desktop\\Archivos\\variables.csv', 'r') as csvfile:   #usamos el manejador de contexto #csvfile solo es un nombre de variable
    lector = csv.reader(csvfile, delimiter=";") #se utiliza el método reader
    encabezado = next(lector)
    # print(encabezado)  
    presion = []
    print(encabezado[3])
    for fila in lector:          #con el for se itera sobre el objeto para leer
        fila[3] = fila[3].replace (",",".")
        dato = float(fila[3])
        presion.append(dato)

print(presion)