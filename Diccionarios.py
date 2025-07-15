
contactos = {}


def agregar_contacto(nombre,celular):
    contactos[nombre] = celular
    print(f"Contacto '{nombre}' agregado")


def buscar_contacto(nombre):
    if nombre in contactos:
        print(f"{nombre}: {contactos[nombre]}")
    else:
        print("No se ha encontrado contacto")

def eliminar_contacto(nombre):
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto '{nombre}' eliminado")
    else:
        print("No se ha encontrado contacto")

def mostrar_contactos():
    for nombre,celular in contactos.items():
        print(f"{nombre}: {celular}")


while True:
    print(" ----------- AGENDA DE CONTACTOS -------------")
    print("1. Agregar Contacto")
    print("2. Buscar Contacto")
    print("3. Eliminar Contacto")
    print("4. Mostrar Contactos")
    print("5. Salir")

    opcion = input("ingrese opcion: ")

    if opcion == "1":
        nombre = input("ingrese nombre: ")
        telefono = input("ingrese telefono: ")
        agregar_contacto(nombre, telefono)

    elif opcion == "2":
        nombre = input("ingrese nombre del contacto a buscar: ")
        buscar_contacto(nombre)

    elif opcion == "3":
        nombre = input("ingrese nombre del contacto a eliminar: ")
        eliminar_contacto(nombre)

    elif opcion == "4":
        mostrar_contactos()

    elif opcion == "5":
        print("Saliendo")
        break
    else:
        print("Opcion no valida")



