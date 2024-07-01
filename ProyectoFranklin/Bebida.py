#Se importa producto de la clase Producto, ya que la clase Bebida hereda de Producto.
from Producto import Producto

'''
Se crea una clase Bebida que hereda de Producto, donde se llama las bebidas alcoholicas,
para mostrar la información de las bebidas alcoholicas.

'''

class Bebida(Producto):
    def __init__(self, nombre, price, stock, alcoholic):
        super().__init__(nombre, price, stock)
        self.alcoholic = alcoholic

#Se retorna el método show() de la clase Producto, añadiendo la información de alcohol   
    def show(self):
        return super().show() + f"\nAlcoholica: {self.alcoholic}"