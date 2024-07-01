class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock


    def show(self):
        return f"-Nombre: {self.nombre}\n-Precio: {self.precio}\n-Stock: {self.stock}\n"

    def getnombre(self):
        return self.nombre

    def getPrecio(self):
        return self.precio

    def getStock(self):
        return self.stock

    def setStock(self, cantidad):
        self.stock = cantidad
        if self.stock < 0:
            self.stock = 0
            print("La cantidad de stock no puede ser negativa")
        

    