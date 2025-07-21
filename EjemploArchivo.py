

nombre_archivo = "archivo.txt"

# Escribir en un Archivo
with open ("archivo.txt",'w') as archivo:
    archivo.write("Primera Linea\n")
    archivo.write("Segunda Linea\n")

# Leer contenido de un Archivo
with open ("archivo.txt",'r') as archivo:
    print(archivo.read())

# Escribe al final de docuemento sin borrar nada
with open ("archivo.txt",'a') as archivo:
    archivo.write("Tercera Linea\n")

#Leer linea por linea
with open ("archivo.txt",'r') as archivo:
    for linea in archivo:
        print(linea)


#-----------------------------------------------
# Crea el Archivo y escribe texto
with open ("ejemplo.txt",'w') as archivo:
    archivo.write("Comienza Primera Linea\n")


