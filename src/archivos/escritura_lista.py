lista = ["Iris","No ordinary life","Hooks","Sextaps","M."]
location = "C:\\Users\\B09S202est\\Desktop\\Archivos"
archive_name = "listas.txt"
mode = "w"
fp = open(location+"\\"+archive_name, mode, encoding="utf-8") 
for song in lista:
    fp.write(song +"\n") #writelines se usa para copiar
fp.close()