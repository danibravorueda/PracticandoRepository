import csv


# Escribir en un Archivo de Tabla
with open("ejemplo.csv",'w',newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Nombre","Edad"])
    escritor.writerow(["dani","30"])
    escritor.writerow(["camila","25"])
    escritor.writerow(["Carmen","35"])

# Leer Archivos
with open("ejemplo.csv",'r') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)

#Escritura Condicional a Archivos

evento = "Error de Red"
with open("log.txt",'w') as archivo:
    if evento == "Error de Red":
        archivo.write("Se detecto un error en Red\n")
