class Venta():
    def __init__(self, id_venta=None, id_producto=None, nombre_producto=None, unidades=None, valor=None, fecha=None):
        self.id_venta = id_venta
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.unidades = unidades
        self.valor = valor
        self.fecha = fecha

    ventas = []

    def get_ventas(self):
        if len(self.ventas) == 0:
            return False
        return self.ventas

    def registrar_venta(self, venta):
        self.ventas.append(venta)
        return venta

    def mostrar_ventas(self):
        if len(self.ventas) != 0:
            return self.ventas
        else:
            return False

    def calcular_total_ventas(self):
        total_ventas = 0
        valor_total  = 0
        for i in range(len(self.ventas)):
            valor_total += self.ventas[i].valor
            total_ventas += 1

        return valor_total, total_ventas





