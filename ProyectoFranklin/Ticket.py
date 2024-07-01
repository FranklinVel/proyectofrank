import uuid

class Ticket:
    def __init__(self, nombre, cedula, edad, tipo, partido, precio, asiento):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.codigo_ticket = uuid.uuid4()
        self.tipo = tipo
        self.partido = partido 
        self.precio = precio 
        self.asiento = asiento
        self.asistencia = False

    def info(self):
        return f"""
        Ticket: {self.codigo_ticket}
        Partido: {self.partido.casa.nombre} vs {self.partido.away.nombre}
        Precio: {self.precio}"""
        
    def vip(self):
        if self.codigo_ticket == "VIP":
            for precio in self.precio:
                precio = "75$"
        elif self.codigo_ticket == "General":
            for precio in self.precio:
                precio = "35$"
                self.precio = precio 
        return precio 
    
    def descuentos(self):
        for cliente in self.codigo_ticket:
            if cliente == "Posee una cedula vampira":
                for precio in self.precio:
                    precio = precio * 0.5