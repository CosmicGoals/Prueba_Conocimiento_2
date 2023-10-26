class ProductoAseo:
    def __init__(self, id, nombre, descripcion, costo, cantidad, margen_de_venta, callback=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.margen_de_venta = margen_de_venta
        self.precio_de_venta = None
        if callback:
            self.asignar_precio_venta(callback)

    def asignar_precio_venta(self, callback):
        if self.margen_de_venta <= 0:
            raise ValueError("El margen de venta debe ser mayor que 0")
        self.precio_de_venta = callback(self.costo, self.margen_de_venta)

class RegistroProductos:
    def __init__(self):
        self.productos = {}

    def registrar_producto(self, producto):
        self.productos[producto.id] = producto

    def imprimir_lista_productos(self):
        print("Listado de Productos de Aseo:")
        for producto in self.productos.values():
            print(f"ID: {producto.id}")
            print(f"Nombre: {producto.nombre}")
            print(f"Descripción: {producto.descripcion}")
            print(f"Costo: ${producto.costo}")
            print(f"Cantidad: {producto.cantidad}")
            print(f"Precio de Venta: ${producto.precio_de_venta}")
            print()


def calcular_precio_venta(costo, margen_de_venta):
    return costo / (1 - margen_de_venta)


if __name__ == '__main__':
    registro = RegistroProductos()
    producto1 = ProductoAseo(1, "Shampoo", "Para cabello normal", 5, 100, 0.2, calcular_precio_venta)
    producto2 = ProductoAseo(2, "Jabón", "Fragancia de lavanda", 2, 200, 0.15, calcular_precio_venta)

    registro.registrar_producto(producto1)
    registro.registrar_producto(producto2)

    registro.imprimir_lista_productos()
