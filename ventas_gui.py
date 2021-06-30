from tkinter import *
from tkinter import messagebox
from random import randint
from datetime import datetime

from peluches import Producto
from ventas import  Venta

class VentasGui:
    def __init__(self, padre, idProducto, ventanaPadre):
        self.padre = padre
        self.ventanaPadre = ventanaPadre
        self.idProducto = idProducto
        self.win = Toplevel(self.ventanaPadre)
        self.win.title("Registar venta")
        self.win.geometry("500x400")
        self.win.resizable(0, 0)
        # self.win.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.crearWidgets()
        self.win.mainloop()

    def generarIDVenta(self):
        id = randint(1, 9999)
        cont = 0
        venta = Venta()
        ventas = venta.mostrar_ventas()

        if ventas:
            for venta in ventas:
                if venta.id_venta == id:
                    cont += 1
            if cont != 0:
                self.generarIDVenta()
            else:
                return id
        else:
            return id

    def destroyWindow(self):
        self.win.destroy()

    def crearWidgets(self):
        # Creating a Frame Container
        self.frameLogo = Frame(self.win)
        self.frameLogo.pack(pady=10)

        # Create image logo
        self.path = './img/venta.png'
        self.imagen = PhotoImage(file=self.path)
        self.img_label = Label(self.frameLogo, image=self.imagen)
        self.img_label.pack(padx=10, pady=20)

        self.frameFather = Frame(self.win)
        self.frameFather.pack()

        self.frameLabels = Frame(self.frameFather)
        self.frameLabels.pack(side=LEFT, pady=30)

        self.frameInputs = Frame(self.frameFather)
        self.frameInputs.pack(side=LEFT)


        self.frameButtons = Frame(self.win)
        self.frameButtons.pack(pady=20)

        # Labels

        self.lblId = Label(self.frameLabels, text="Identificador: ", font="sans 12")
        self.lblId.pack(side=TOP, padx=20)

        self.lblUnidades = Label(self.frameLabels, text="Unidades a vender: ", font="sans 12")
        self.lblUnidades.pack(side="bottom", padx=22)

        self.lblPrecio = Label(self.frameLabels, text="Precio: ", font="sans 12")
        self.lblPrecio.pack(side="bottom", padx=22)

        self.lblCantidad = Label(self.frameLabels, text="Cantidad: ", font="sans 12")
        self.lblCantidad.pack(side="bottom", padx=22)

        self.lblNombre = Label(self.frameLabels, text="Nombre: ", font="sans 12")
        self.lblNombre.pack(side="bottom", padx=22)


        # Inputs
        producto = Producto()
        item = producto.obtenerProducto(self.idProducto)

        self.entryId = Entry(self.frameInputs, textvariable = StringVar(value = item.id), state = 'readonly')
        self.entryId.pack()

        self.entryNombre = Entry(self.frameInputs, textvariable = StringVar(value = item.nombre), state = 'readonly')
        self.entryNombre.pack(pady=2)

        self.entryCantidad = Entry(self.frameInputs, textvariable = StringVar(value = item.cantidad), state = 'readonly')
        self.entryCantidad.pack(pady=2)

        self.entryPrecio = Entry(self.frameInputs, textvariable = StringVar(value = item.precio), state = 'readonly')
        self.entryPrecio.pack()

        self.entryUnidades = Entry(self.frameInputs)
        self.entryUnidades.focus()
        self.entryUnidades.pack()

        # Buttons
        self.buttonAgregar = Button(self.frameButtons, text='Registrar venta', command=self.venderProducto).pack(side=LEFT,padx=20)
        self.buttonCancelar = Button(self.frameButtons, text='Cancelar', command=self.destroyWindow).pack(side=LEFT)

    def venderProducto(self):
        try:
            id_producto = self.idProducto
            nombre_producto = self.entryNombre.get()
            unidades = int(self.entryUnidades.get())
            precioUnidad = int(self.entryPrecio.get())
            precio_final = unidades * precioUnidad

            producto = Producto(id_producto)

            if producto.validar_existencia_unidades(unidades):
                message = f'Confirmar compra?\n' \
                          f'Unidades: {unidades}\n' \
                          f'Precio final: ${precio_final} COP'
                if messagebox.askokcancel("", message):
                    producto.set_cantidad(unidades)
                    id_venta = self.generarIDVenta()
                    producto.comprobar_inventario()
                    now = datetime.now()
                    fecha = now.strftime("%d/%m/%Y %H:%M:%S")
                    venta = Venta(id_venta, id_producto, nombre_producto, unidades, precio_final, fecha)
                    venta.registrar_venta(venta)

                    self.destroyWindow()
                    messagebox.showinfo(":)", "La venta se registro exitosamente")
                    self.padre.get_products()
                    self.padre.cambiarEstadoBotones()

            else:
                message = "El número de unidades a vender es mayor al inventario disponible"
                messagebox.showerror(":(", message)

        except ValueError:
            message = "El campo unidades debe ser un valor númerico entero"
            messagebox.showerror(":(", message)




