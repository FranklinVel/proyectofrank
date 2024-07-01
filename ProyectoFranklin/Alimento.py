#Se importa de la clase Produtcto la clase Producto, ya que la clase Alimento hereda de Producto.
from Producto import Producto

#Clase Alimento que hereda de Producto, la cual tiene un paquete adicional.
class Alimento(Producto):
    def __init__(self, nombre, price, stock, package):
        super().__init__(nombre, price, stock)
        self.package = package

#Se retorna los detalles del alimento, heredado de la clase Producto.
    def show(self):
        return super().show() + f"\nPaquete: {self.package}"