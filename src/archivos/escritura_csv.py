import csv

encabezado1 = ["Ingresos", "Egresos"]
renglon1  = [10000,15000]
renglon2  = [11000,14000]
renglon3  = [15000,0]
renglon4  = [14000,7000]
renglon5  = [5000,2000]
renglon6  = [10000,5000]
renglon7  = [20000,2000]


with open('.//src//archivos//salida.csv', 'w', newline='') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(encabezado1)  # Escribe la fila de encabezados
    escritor.writerow(renglon1)
    escritor.writerow(renglon2)
    escritor.writerow(renglon3)
    escritor.writerow(renglon4)
    escritor.writerow(renglon5)
    escritor.writerow(renglon6)
    escritor.writerow(renglon7)
