class Clientes: 

    def __init__(self, nombre, cedula, edad ):
        self.nombre = nombre 
        self.cedula = cedula 
        self.edad = edad 

        def __str__():
            return f"Nombre: {self.nombre}, Cedula: {self.cedula}, Edad: {self.edad}"
        
    def es_vampiro(self):
        str_cedula = str(self.cedula)
        digitos_cedula = len(str_cedula)

        if digitos_cedula % 2 != 0:
            return False
        
        digitos_factor = digitos_cedula // 2
        
        for i in range(10**(digitos_factor-1), 10**digitos_factor):
            for j in range(i, 10**digitos_factor):
                if i * j == self.cedula:
                    cadena_factor = str(i) + str(j)
                if set(str_cedula) == set(cadena_factor):
                    return True
                
        return False