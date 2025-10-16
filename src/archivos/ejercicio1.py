fp = open("./src/archivos/texto.txt","r")
"""
datos = fp.read(5)
print(datos)
datos = fp.read(5)
print(datos)
"""
"""
fp.readline()
fp.readline()
"""
fp.seek(10)
datos = fp.readline()
print(datos) 
fp.close()
