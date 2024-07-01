#Se crea la clase partido con sus atributos.
class Partido:
        def __init__(self, id, numero, casa, away, fecha, grupo, estadio):
                self.id = id
                self.numero = numero
                self.casa = casa
                self.away = away
                self.fecha = fecha
                self.grupo = grupo
                self.estadio = estadio
        
        def mostrar(self):
                return f"-Equipo Local: {self.casa.nombre}\n-Equipo Visitante: {self.away.nombre}\n-Fecha: {self.fecha}\nEstadio: {self.estadio.mostrar()}\n"


