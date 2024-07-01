'''

Se importan las clases necesarias, y se define la clase 'App' 
que contiene todas las instancias de las clases definidas anteriormente.

'''
from validaciones import *
from Alimento import Alimento
from Bebida import Bebida
from Boleto import Boleto
from Cliente import Clientes
from Equipo import Equipo
from Estadio import Estadio
from Factura import Factura
from Partido import Partido
from Producto import Producto
from Restaurante import Restaurante
from Ticket import Ticket 
import requests
'''
Se crea la clase App, donde estaran instancias de cada clase y se agregan a una lista vacia
correspondiente para almacenar los objetos de cada clase.
'''
class App:
    def __init__(self):
        self.alimentos = []
        self.bebidas = []
        self.boletos = []
        self.clientes = []
        self.equipos = []
        self.estadios = []
        self.facturas = []
        self.partidos = []
        self.restaurantes = []
        self.productos = self.alimentos + self.bebidas
        


#Se define un metodo en la clase App para cargar los equipos, estadios y partidos desde una API.

    '''
    Se define cargar_equipos que se encarga de obtener los equipos desde una API y 
    los agrega a la lista de equipos, con sus respectivos atributos y siendo objetos de la clase Equipo.

    '''

    def cargarEquipos(self):
            response = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json")
            data = response.json()

            for dict in data:
                id = dict["id"]
                codigo = dict["code"]
                nombre = dict["name"]
                grupo = dict["group"]

                equipo = Equipo(id, codigo, nombre, grupo)
                self.equipos.append(equipo)
    '''
    Se define cargar_estadios que se encarga de obtener los estadios desde una API y
    los agrega a la lista de estadios, con sus respectivos atributos y siendo objetos de la clase Estadio.
    '''

    def llenarMapa(self, capacidad):
        mapa = []

        letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        
        count = 1
        while capacidad > 0:
            if capacidad < 10:
                lista = []
                for idx, _ in enumerate(range(1, capacidad+1)):
                    lista.append([f"{count}{letras[idx]}"])

            else:
                lista = []
                for letra in letras:
                    lista.append([f"{count}{letra}"])

            mapa.append(lista)  
            capacidad -= 10
            count += 1
        
        return mapa




    def cargarEstadios(self):
            response = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json")
            data = response.json()
            
            for dict in data:
                id = dict["id"]
                nombre = dict["name"]
                ciudad = dict["city"]
                mapaGeneral = self.llenarMapa(dict["capacity"][0])
                mapaVip = self.llenarMapa(dict["capacity"][1])
                restaurantes = []

                for inforest in dict["restaurants"]:
                    nombreRestaurant = inforest["name"]
                    productos = []

                    for infoProducto in inforest["products"]:
                        nombreProducto = infoProducto["name"]
                        precio = float(infoProducto["price"]) + (float(infoProducto["price"])*0.16)
                        stock = int(infoProducto["stock"])

                        if infoProducto["adicional"] == "plate":
                            package = False
                            productos.append(Alimento(nombreProducto, stock, precio, package))
                            self.productos.append(Alimento(nombreProducto, stock, precio, package))
                        elif infoProducto["adicional"] == "package":
                            package = True
                            productos.append(Alimento(nombreProducto, stock, precio, package))
                            self.productos.append(Alimento(nombreProducto, stock, precio, package))
                        elif infoProducto["adicional"] == "alcoholic":
                            productos.append(Bebida(nombreProducto, stock, precio, True))
                            self.productos.append(Bebida(nombreProducto, stock, precio, True))
                        else:
                            productos.append(Bebida(nombreProducto, stock, precio, False))
                            self.productos.append(Bebida(nombreProducto, stock, precio, False))
                    
                    restaurant = Restaurante(nombreRestaurant, productos)
                    self.restaurantes.append(restaurant)
                    restaurantes.append(restaurant)
                
                estadio = Estadio(id, nombre, ciudad, mapaGeneral, mapaVip, restaurantes)
                self.estadios.append(estadio)

    def buscarEquipoId(self, id):
        for equipo in self.equipos:
            if equipo.getid() == id:
                return equipo
        return None
    
    def buscarEstadioId(self, id):
        for estadio in self.estadios:
            if estadio.getid() == id:
                return estadio
        return None
                              
    def cargarPartidos(self):
            response = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json")
            data = response.json()
            
            for dict in data:
                id = dict["id"]
                nombre = dict["number"]
                casa = self.buscarEquipoId(dict["home"]["id"])
                visitante = self.buscarEquipoId(dict["away"]["id"])
                fecha = dict["date"]
                grupo = dict["group"]
                estadio = self.buscarEstadioId(dict["stadium_id"])
                
                partido = Partido(id, nombre, casa, visitante, fecha, grupo, estadio)
                self.partidos.append(partido)
                
    def cargar(self):
        self.cargarEquipos()
        self.cargarEstadios()
        self.cargarPartidos()
        print("\nCarga Exitosa\n")

    def verEquipos(self):
        print("\n")
        for equipo in self.equipos:
            print(equipo.mostrar())

    def verEstadios(self):
        print("\n")
        for estadio in self.estadios:
            print(estadio.mostrar())

    def verPartidos(self):
        print("\n")
        for partido in self.partidos:
            print(partido.mostrar())


    def buscarPartidosPorEquipo(self, nombre):
        resultado = []
        for partido in self.partidos:
            if nombre in partido.casa.getnombre().lower() or nombre in partido.away.getnombre().lower():
                resultado.append(partido)
        
        print("\n")
        if len(resultado) != 0:
            for partido in resultado:
                print(partido.mostrar())
        else:
            print("\nNo se encontraron partidos para el equipo ingresado.")

    def buscarPartidosPorEstadio(self, nombreEstadio):
        resultado = []
        for partido in self.partidos:
            if nombreEstadio in partido.estadio.nombre.lower() or nombreEstadio in partido.estadio.nombre.lower():
                resultado.append(partido)
        
        print("\n")
        if len(resultado) != 0:
            for partido in resultado:
                print(partido.mostrar())
        else:
            print("\nNo se encontraron partidos para el equipo ingresado.")

    
    def buscarPartidosPorFecha(self, fecha):
        resultado = []
        for partido in self.partidos:
            fechaSeparada = partido.fecha.split("-")
            if fechaSeparada[2] == fecha:
                resultado.append(partido)

        print("\n")
        if len(resultado) != 0:
            for partido in resultado:
                print(partido.mostrar())
        else:
            print("\nNo se encontraron partidos para el equipo ingresado.")

 
    def buscarPartidos(self):
        while True:
            print("\n====================")
            print("BUSQUEDA DE PARTIDOS")
            print("====================")
            print("1. Por Equipo\n2. Por Estadio\n3. Por Fecha\n4. Salir")
            
            option = opciones(4, "Ingrese el número correspondiente a la acción que desea realizar: ")
            
                
            if option == 1:
                nombre = validar_str("Ingrese el nombre del equipo para filtrar los partidos: ").lower()
                
                self.buscarPartidosPorEquipo(nombre)
            elif option == 2:
                nombreEstadio = validar_str("Ingresa el nombre del estadio para filtrar los partidos: ").lower()
                
                self.buscarPartidosPorEstadio(nombreEstadio)
            elif option == 3:
                fecha = input("Ingrese el dia para filtrar los partidos: ")
                while not fecha.isnumeric() or not range(14, 27):
                    print("Error!!! Dato Inválido.")
                    fecha = input("Ingrese el dia para filtrar los partidos: ")

                self.buscarPartidosPorFecha(fecha)
            elif option == 4:
                break

    def gestionPartidos(self):
        while True:
            print("\n==============================")
            print("GESTION DE PARTIDOS Y ESTADIOS")
            print("==============================")
            print("1. Ver Equipos\n2. Ver Estadios\n3. Ver Partidos\n4. Buscar Partidos\n5. Salir")
            
            option = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            while (not option.isnumeric()) or (not int(option) in range(1,6)):
                print("Error!!! Dato Inválido.")
                option = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            
                
            if option == "1":
                self.verEquipos()
            elif option == "2":
                self.verEstadios()
            elif option == "3":
                self.verPartidos()
            elif option == "4":
                self.buscarPartidos()
            else:
                print("\nAdiós.")
                break       


    def gestionVentasEntradas(self):


         # Mostrar partidos disponibles, deja que el usurio escoka que si indiice o algo ais
         # cuando escoja el partido, busca el estado en el que se hace
         # Pregunta al usuario si quiere vip o general
         # Muestra el mapa vip o general del estadio edl partido, que escoja el asiento
         # Sigues con el modulo como te dice

         #PARA EL OBJETO DE BOLETO pendiente con los atributos, appendealo a la lista de boleto
        print("\n========================================")
        print("            REGISTRAR CLIENTE")
        print("========================================")

        nombre = validar_str("Ingrese nombre del cliente: ")
        
        cedula = validar_int("Ingrese cedula del cliente: ")

        edad = validar_int("Ingrese edad del cliente: ")
        
        cliente = Clientes(nombre, cedula, edad)
        self.clientes.append(cliente)
        print("\nCliente registrado exitosamente.")

        print("\n===============================")
        print("        ELEGIR PARTIDO")
        print("===============================\n")

        for count, partido in enumerate(self.partidos):
            print(f"{count}.\n{partido.mostrar()}")
        
        opcionPartido = opciones(len(self.partidos),
        "Ingrese el numero del partido al que desea asistir: ")
    
        partidoElegido = self.partidos[opcionPartido-1]

        print("\n================================")
        print("     ELEGIR TIPO DE ENTRADA")
        print("================================")

        print("1. General\n2. Vip")
        
        opcionEntrada = opciones(2, "Ingrese el número correspondiente al tipo de entrada: ")
        
        estadioDelPartido = partidoElegido.estadio

        if opcionEntrada == 1:
            entrada = "General"
            subtotal = 35
            mapa = estadioDelPartido.mapaGeneral

            #Ahora debes mostrar el mapa general del estadio para que el cliente elija su puesto
        else:
            entrada = "VIP"
            subtotal = 75
            mapa = estadioDelPartido.mapaVip

            #Ahora debes mostrar el mapa vip del estadio para que el cliente elija su puesto
        for asiento in mapa:
            print(asiento)

        asiento = validar_asiento(mapa)

        if numero_vapiro(cedula):
            subtotal -= (subtotal*50)/100
        
        subtotal += (subtotal*16)/100
        

        ticket = Ticket(
            nombre,
            cedula, 
            edad,
            entrada,
            partidoElegido,
            subtotal,
            asiento
        )

        self.boletos.append(ticket)
        print(ticket.info())
        

    def gestionAsistencia(self):
        codigo = input("Ingrese el codigo del boleto: ")

        ticket = None
        for boleto in self.boletos:
            if str(boleto.codigo_ticket) == codigo:
                ticket = boleto
        
        if ticket == None:
            print("El ticket no esta registrado")
        else:  
            if ticket.asistencia == True:
                print("El ticket ya fue usado")
            else:
                ticket.asistencia = True
                print("Se ha confirmado la asistencia al partido del cliente!!!")
        

    def verProductos(self):
        for producto in self.productos:
            print(producto.show())

    def buscarProductoNombre(self, nombre):
        resultado = []
        for producto in self.productos:
            if nombre.lower() in producto.nombre.lower():
                resultado.append(producto)

        if len(resultado) != 0:
            for producto in resultado:
                print(producto.show())
        else:
            print("\nNo se encontraron productos para el nombre ingresado.")

    
    def buscarAlimento(self):
        resultado = []
        for producto in self.productos:
            if isinstance(producto, Alimento):
                resultado.append(producto)

        if len(resultado)!= 0:
            nombre = ("Ingrese el nombre del alimento: ").lower()
            while (not nombre.isalpha()) or (not len(nombre) >= 1):
                print("Error!!! Dato Inválido.")
                nombre = input("\nIngrese el nombre del alimento: ").lower()

            resultadoNombre = []
            for producto in resultado:
                if nombre.lower() in producto.nombre.lower():
                    resultadoNombre.append(producto)
            
            if len(resultadoNombre)!= 0:
                for producto in resultadoNombre:
                    print(producto.show())

            else:
                print("\nNo se encontraron alimentos para el nombre ingresado.")
            
        else:
            print("\nNo se encontraron alimentos.")


        

    def buscarBebida(self):
        resultado = []
        for producto in self.productos:
            if isinstance(producto, Bebida):
                resultado.append(producto)

        if len(resultado)!= 0:
            nombre = ("Ingrese el nombre de la bebdia: ").lower()
            while (not nombre.isalpha()) or (not len(nombre) >= 1):
                print("Error!!! Dato Inválido.")
                nombre = input("\nIngrese el nombre de la bebdia: ").lower()

            resultadoNombre = []
            for producto in resultado:
                if nombre.lower() in producto.nombre.lower():
                    resultadoNombre.append(producto)
            
            if len(resultadoNombre)!= 0:
                for producto in resultadoNombre:
                    print(producto.show())

            else:
                print("\nNo se encontraron bebidas para el nombre ingresado.")
            
        else:
            print("\nNo se encontraron bebidas.")




    def buscarProductoTipo(self):
        while True:
            print("1. Alimentos\n 2. Bebidas\n 3. Salir")

            option = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            while (not option.isnumeric()) or (not int(option) in range(1,4)):
                print("Error!!! Dato Inválido.")
                option = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            
                
            if option == "1":
                self.buscarAlimento()
                break
            elif option == "2":
                self.buscarBebida()
            else:
                break



    def buscarProductoPrecio(self, minimo, maximo):
        resultado = []
        for producto in self.productos:
            if (int(minimo) <= producto.precio) and (int(maximo) >= producto.precio):
                resultado.append(producto)

        if len(resultado)!= 0:
            for producto in resultado:
                print(producto.show())
        else:
            print("\nNo se encontraron productos con precios dentro del rango ingresado.")




    def buscarProductos(self):
        while True:
            print("\n=====================")
            print("BUSQUEDA DE PRODUCTOS")
            print("=====================")
            print("1. Por Nombre\n2. Por Tipo\n3. Por Rango de Precio\n4. Salir")
            
            option = opciones(4, "Ingrese el número correspondiente a la acción que desea realizar: ")
            
                
            if option == 1:
                nombre = validar_str("Ingrese el nombre del producto: ").lower()
                
                self.buscarProductoNombre(nombre)
            elif option == 2:
                
                self.buscarProductoTipo()
            elif option == 3:
                minimo = validar_int("Ingrese el precio minimo: ")

                maximo = validar_int("Ingrese el precio maximo: ")

                self.buscarPartidosPorFecha(minimo, maximo)
            elif option == 4:
                break    



    def gestionRestaurant(self):
        while True:
            print("\n=====================")
            print("GESTION DE RESTAURANT")
            print("=====================")
            print("1. Ver Productos\n2. Buscar Productos\n3. Salir")
            
            option = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            while (not option.isnumeric()) or (not int(option) in range(1,4)):
                print("Error!!! Dato Inválido.")
                option = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            
                
            if option == "1":
                self.verProductos()
            elif option == "2":
                self.buscarProductos()
            else:
                break



    def gestionVentaRestaurant(self):
        cedula = validar_int("Ingrese cedula del cliente: ")

        find = False
        for boleto in self.boletos:
            print(boleto.cedula)
            if str(boleto.cedula) == str(cedula) and boleto.tipo == "VIP":
                find = True

                if boleto.edad > 18:
                
                    for idx, producto in enumerate(self.productos):
                        print(f"{idx}. {producto.nombre}: {producto.precio}")
                    
                    indice_producto = opciones(len(self.productos), "Ingrese el numero del producto deseado: ")
                    producto_seleccionado = self.productos[indice_producto-1]

                    cantidad = validar_int("Ingrese la cantidad del producto")
                    while cantidad < 0:
                        print("Dato no valido!")
                    while cantidad >= producto_seleccionado.stock:
                        print("No hay suficiente stock para la cantidad deseada: ")
                    

                    total = producto_seleccionado.precio * cantidad
                    if numero_perfecto(cedula):
                        total = (total * 15)/100


                    print("Desea realizar la compra?\n1.Si\n2.No")
                    opcion = opciones(2, "Ingrese el numero de la opcion deseada: ")

                    if opcion == 1:                    
                        producto_seleccionado.stock -= cantidad
                        factura = Factura(cedula, producto_seleccionado, cantidad, total)
                        self.facturas.append(factura)
                        factura.info()
                        print("La compra se ha realizado con exito!")
                
                else:
                    productos_menor = []

                    for producto in self.productos:
                        if isinstance(producto, Bebida):
                            if not producto.alcoholic:
                                productos_menor.append(producto)
                        else:
                            productos_menor.append(producto)

                    for idx, p in enumerate(productos_menor):
                        print(f"{idx}. {p.nombre}: {p.precio}$")

                    
                    indice_producto = opciones(len(productos_menor), "Ingrese el numero del producto deseado: ")
                    producto_seleccionado = productos_menor[indice_producto-1]

                    cantidad = validar_int("Ingrese la cantidad del producto: ")
                    while cantidad < 0:
                        print("Dato no valido!")
                    while cantidad >= producto_seleccionado.stock:
                        print("No hay suficiente stock para la cantidad deseada")
                    

                    total = producto_seleccionado.precio * cantidad
                    if numero_perfecto(cedula):
                        total = (total * 15)/100


                    print("Desea realizar la compra?\n1.Si\n2.No")
                    opcion = opciones(2, "Ingrese el numero de la opcion deseada: ")

                    if opcion == 1:                    
                        producto_seleccionado.stock -= cantidad
                        factura = Factura(cedula, producto_seleccionado, cantidad, total)
                        self.facturas.append(factura)

                        factura.info()
                        print("La compra se ha realizado con exito!")
                break
        
        if not find:
            print("Cliente no registrado")
                
                




    def indicadoresGestion(self):
        pass




    def menu(self):
        self.cargar()

        print("\n")
        while True:
            print("\n===============================")
            print("BIENVENIDOS PROYECTO EURO 2024")
            print("===============================")
            print("1. Gestión de partidos y estadios\n2. Gestión de venta de entradas\n3. Gestión de asistencia a partidos\n4. Gestión de restaurantes\n5. Gestión de venta de restaurantes\n6. Indicadores de Gestión\n7. Salir")
            
            option = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            while (not option.isnumeric()) or (not int(option) in range(1,8)):
                print("Error!!! Dato Inválido.")
                option = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            
                
            if option == "1":
                self.gestionPartidos()

            elif option == "2":
                self.gestionVentasEntradas()   

            elif option == "3":
                self.gestionAsistencia()

            elif option == "4":
                self.gestionRestaurant()
            elif option == "5":
                self.gestionVentaRestaurant()
            elif option == "6":
                self.indicadoresGestion()
            else:
                print("\nAdiós.")
                break       



def numero_vapiro(n):
    numero_str = str(n)
    longitud = len(numero_str)
    
    if longitud % 2 != 0:
        return False
    
    mitad = longitud // 2
    fangs = []
    
    from itertools import permutations
    for perm in permutations(numero_str):
        x = int(''.join(perm[:mitad]))
        y = int(''.join(perm[mitad:]))

        if x * y == n and not (str(x).endswith('0') and str(y).endswith('0')):
            fangs.append((x, y))
    
    return len(fangs) > 0


def numero_perfecto(n):
    if n < 2:
        return False
    
    suma_divisores = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            suma_divisores += i
            if i != n // i:
                suma_divisores += n // i
    
    return suma_divisores == n



