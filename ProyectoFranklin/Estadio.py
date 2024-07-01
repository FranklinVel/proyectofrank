#Se crea la clase Estadio con sus respectivos atributos.
class Estadio:

        def __init__(self, id, nombre, ciudad, mapaGeneral, mapaVip, restaurantes ):
                self.id = id 
                self.nombre = nombre
                self.ciudad = ciudad
                self.mapaGeneral  = mapaGeneral
                self.mapaVip = mapaVip
                self.restaurantes = restaurantes
        
        def mostrar(self):
                return f"-Nombre: {self.nombre}\n-Ubicacion: {self.ciudad}\n"
        
        def getid(self):
                return self.id