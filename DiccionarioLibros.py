
libros = {}

def agregar_libros(titulo,autor,ano):
    if autor in libros:
        print("El libro ya existe")
    else:
        libros[titulo]={"autor":autor,"ano":ano}
        print(f"El Libro '{titulo}' se creo correctamente'")

def buscar_libros(titulo):
    if titulo in libros:
      print(libros[titulo])
    else:
        print(f"El libro '{titulo}' no existe")


def eliminar_libros(titulo):
    if titulo in libros:
        del libros[titulo]
    else:
        print(f"El libro '{titulo}' no existe")

def mostrar_libros():
    for titulo,datos in libros.items():
        print(f"{titulo} ({datos['ano']}) por {datos['autor']}")



while True:
    print("-------- BIBLIOTECA -------------")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Mostrar libros")
    print("5. Salir")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        titulo = input("Ingrese el titulo: ")
        autor = input("Ingrese el autor: ")
        ano = input("Ingrese el año: ")
        agregar_libros(titulo,autor,ano)

    elif opcion == "2":
        titulo = input("Ingrese el titulo del libro a buscar: ")
        buscar_libros(titulo)

    elif opcion == "3":
        titulo = input("Ingrese el titulo del libro a eliminar: ")
        eliminar_libros(titulo)

    elif opcion == "4":
        mostrar_libros()

    elif opcion == "5":
        print("Saliendo")
        break

    else:
        print("Opcion no valida")
