
class Producto:
    def __init__(self, id=None, nombre=None, cantidad=None, precio=None):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    productos = []

    def agregarProductos(self, producto):
        self.productos.append(producto)
        return True

    def getProductos(self):
        if len(self.productos) == 0:
            return False
        return self.productos

    def validarProducto(self):
        for producto in self.productos:
            if producto.id == self.id:
                return True
        return False

    def eliminarProducto(self, id):
        for i in range(len(self.productos)):
            if self.productos[i].id == id:
                self.productos.pop(i)
                return True

        return False

    def obtenerProducto(self, id):
        for producto in self.productos:
            if producto.id == id:
                return producto
        return False

    def modificar_producto(self, producto):
        for i in range(len(self.productos)):
            if self.productos[i].id == producto.id:
                self.productos[i] = producto
                return True

        return False

    def validar_existencia_unidades(self, unidades):
        for producto in self.productos:
            if producto.id == self.id:
                if producto.cantidad >= unidades:
                    return True
                else:
                    return False

    def set_cantidad(self, unidades):
        for producto in self.productos:
            if producto.id == self.id:
                producto.cantidad -= unidades
        return False

    def comprobar_inventario(self):
        for i in range(len(self.productos)):
            if self.productos[i].id == self.id:
                if self.productos[i].cantidad == 0:
                    self.productos.pop(i)
                    return True
                else:
                    return False

