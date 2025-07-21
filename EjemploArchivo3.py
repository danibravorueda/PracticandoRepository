
import json

#Escribir un archivo JSON
datos = {"nombre":"Marcelo", "edad":30}

with open("datos.json",'w', newline='') as archivo_json:
    json.dump(datos,archivo_json)

#Leer Archivos JSON
with open('datos.json','r') as archivo_json:
    contenido = json.load(archivo_json)
    print(contenido)