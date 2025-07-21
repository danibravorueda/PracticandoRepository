


class Encapsulamiento:

    def __init__(self,nombre,precio):
        self.__nombre=nombre
        self.__precio=precio

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def set_precio(self,precio):
        if precio >0:
            self.__precio+=precio
            print(f" Se agrego el precio de '{self.__precio}' correctamente")
        else:
            print("Precio negativo")


producto = Encapsulamiento("Cosa",234)
print(producto.get_nombre())

producto.set_precio(-100)
