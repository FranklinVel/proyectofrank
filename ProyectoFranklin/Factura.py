class Factura:
    def __init__(self, cedula, producto, cantidad, total):
        self.cedula = cedula
        self.producto = producto
        self.cantidad = cantidad
        self.total = total
    

    def info(self):
        print(f"""
        Nombre: {self.cedula}
        Producto: {self.producto.nombre}
        Cantidad: {self.cantidad}
        Total: {self.total}
        """)