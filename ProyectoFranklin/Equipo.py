#Se crea la clase equipo con sus respectivos atributos. 

class Equipo: 
    
# Constructor del equipo con los atributos id, codigo, nombre y grupo. 
    
    def __init__(self, id, codigo, nombre, grupo):
        self.id = id
        self.codigo = codigo 
        self.nombre = nombre
        self.grupo = grupo
        

    #Se crea el metodo getid para obtener el id del equipo. 
    def getid(self):
        return self.id
    #Se crea el metodo getcodigo para obtener el codigo del equipo. 
    def getcodigo(self):
        return self.codigo
    #Se crea el metodo getnombre para obtener el nombre del equipo.
    def getnombre(self):
        return self.nombre
    #Se crea el metodo getgrupo para obtener el grupo del equipo. 
    def getgrupo(self):
        return self.grupo
    #Se crea el metodo setid para establecer el id del equipo. 
    def setid(self, id):
        self.id = id
    #Se crea el metodo setcodigo para establecer el codigo del equipo. 
    def setcodigo(self, codigo):
        self.codigo = codigo
    #Se crea el metodo setnombre para establecer el nombre del equipo. 
    def setnombre(self, nombre):
        self.nombre = nombre
    #Se crea el metodo setgrupo para establecer el grupo del equipo. 
    def setgrupo(self, grupo):
        self.grupo = grupo
    
    def mostrar(self):
        return f"-Nombre: {self.nombre}\n-Codigo: {self.codigo}\n-Grupo: {self.grupo}\n"