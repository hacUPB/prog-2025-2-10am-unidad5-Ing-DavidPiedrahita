location = "C:\\Users\\B09S202est\\Desktop\\Archivos"
# \ (backslash) se usa para comandos de texto. Uno solo se interpreta mal, se necesitan dos para las rutas de los archivos
archive_name = "Frutas.txt"
"""mode = "a" """# w: solo escritura, sobreescribe. a: escribe sin borrar lo anterior
while True:
    option = input("escribir: a, sobreescribir: w, finalizar:e\n")
    match option:
        case "a":
            mode = "a"
            fp = open(location+"\\"+archive_name, mode, encoding="utf-8") #encoding="utf-8" es una codificación que interpreta las tíldes
            words = input("Ingrese su nombre:\n")
            num = str(float(input("Ingrese su estatura:\n")))
            # text = "Hola " + words +", su estatura es " + num + "m"
            fp.write("Hola " + words +",\nsu estatura es " + num + "m\n")#este metodo write sirve para escribir
            fp.close()
        case "w":
            mode = "w"
            fp = open(location+"\\"+archive_name, mode, encoding="utf-8") #encoding="utf-8" es una codificación que interpreta las tíldes
            words = input("Ingrese su nombre:\n")
            num = str(float(input("Ingrese su estatura:\n")))
            # text = "Hola " + words +", su estatura es " + num + "m"
            fp.write("Hola " + words +",\nsu estatura es " + num + "m\n")#este metodo write sirve para escribir
            fp.close()
        case "e":
            print("Saliendo...")
            break