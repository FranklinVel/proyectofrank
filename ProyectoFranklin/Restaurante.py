#Se crea la clase restaurante con sus atributos y métodos
class Restaurante:
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos
    
    def getnombre(self):
        return self.nombre
    
    def getProducts(self):
        return self.products
    
    def setnombre(self, nombre):
        self.nombre = nombre
        return "Nombre actualizado exitosamente"
    def setproductos(self, productos):
        self.products = productos
        return "Productos actualizados exitosamente"
'''
Se define showProducts para mostrar los productos de cada restaurante y se ejecuta la función
agregando un nuevo producto al restaurante



'''
def showProducts(self):
    products = ""
    for product in self.products:
        products += product.show() + "\n"
