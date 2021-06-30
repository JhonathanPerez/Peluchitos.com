from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

from productos import Producto
from anadir_producto import AnadirProducto
from modificar_producto import  ModificarProducto
from ventas import Venta
from ventas_gui import VentasGui

class Inventario():
    def __init__(self, padre, ventanaPadre):
        self.padre = padre
        self.ventanaPadre = ventanaPadre
        self.win = Toplevel(self.ventanaPadre)
        self.win.title("Inventario")
        self.win.geometry("500x500")
        self.win.resizable(0, 0)
        self.crearWidgets()
        self.get_products()
        self.cambiarEstadoBotones()
        self.win.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.win.mainloop()

    producto = Producto()

    def destroyWindow(self):
        self.ventanaPadre.deiconify()
        self.padre.clearInput()
        self.win.destroy()

    def cambiarEstadoBotones(self):
        if not self.producto.getProductos():
            self.buttonModificar['state'] = DISABLED
            self.buttonEliminar['state'] = DISABLED
            self.buttonVender['state'] = DISABLED
        else:
            self.buttonModificar['state'] = NORMAL
            self.buttonEliminar['state'] = NORMAL
            self.buttonVender['state'] = NORMAL

    def crearWidgets(self):
        # Creating a Frames

        self.frameLogo = Frame(self.win)
        self.frameLogo.pack(fill=BOTH, pady=10)

        self.frameTreeView = Frame(self.win)
        self.frameTreeView.pack(fill=BOTH, pady=10)

        self.frameButtons= Frame(self.win)
        self.frameButtons.pack(pady=10)

        # Create image logo
        self.path = './img/inventario.png'
        self.imagen = PhotoImage(file=self.path)
        self.img_label = Label(self.frameLogo, image=self.imagen)
        self.img_label.pack(padx=10, pady=20)

        # Table
        self.tree = ttk.Treeview(self.frameTreeView)
        self.tree['columns'] = ('Id', 'Nombre', 'Cantidad', 'Precio')
        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('Id', anchor=CENTER, width=80)
        self.tree.column('Nombre', anchor=CENTER, width=80)
        self.tree.column('Cantidad', anchor=CENTER, width=80)
        self.tree.column('Precio', anchor=CENTER, width=80)

        self.tree.heading('#0', text='', anchor=CENTER)
        self.tree.heading('Id', text='Id', anchor=CENTER)
        self.tree.heading('Nombre', text='Nombre', anchor=CENTER)
        self.tree.heading('Cantidad', text='Cantidad', anchor=CENTER)
        self.tree.heading('Precio', text='Precio', anchor=CENTER)

        self.tree.pack(fill=X)

        # Buttons
        self.buttonAnadir = Button(self.frameButtons, text='Añadir', command=self.crearProducto).pack(side=LEFT)

        self.buttonModificar = Button(self.frameButtons, text='Modificar', command=self.modificarProducto)
        self.buttonModificar.pack(side=LEFT, padx=20)

        self.buttonEliminar = Button(self.frameButtons, text='Eliminar', command= self.eliminarProducto)
        self.buttonEliminar.pack(side=LEFT)

        self.buttonVender = Button(self.frameButtons, text='Vender', command=self.registrarVenta)
        self.buttonVender.pack(side=LEFT, padx=20)

        self.buttonSalir = Button(self.frameButtons, text='Salir', command=self.destroyWindow)
        self.buttonSalir.pack(side=LEFT)

    # Get Products from the list


    def get_products(self):
        # cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        # getting data
        productos = self.producto.getProductos()
        if productos == False:
            messagebox.showwarning("","El inventario está vacio :(")
        else:
            for producto in productos:
                self.tree.insert('', 0, text='', values=(producto.id, producto.nombre, producto.cantidad, producto.precio))

    def on_closing(self):
        if messagebox.askokcancel("Salir", "Estás seguro que deseas salir?"):
            self.ventanaPadre.deiconify()
            self.padre.clearInput()
            self.win.destroy()

    def crearProducto(self):
        producto = AnadirProducto(self, self.win)

    def eliminarProducto(self):
        try:
            id = self.tree.item(self.tree.selection())['values'][0]
            if messagebox.askokcancel("Eliminar", "Estás seguro que deseas eliminar el producto?"):
                if self.producto.eliminarProducto(int(id)):
                    message = "El producto fué eliminado correctamente"
                    messagebox.showinfo("", message)
                    self.get_products()
                    self.cambiarEstadoBotones()
        except IndexError as e:
            messagebox.showinfo("","Debe seleccionar un producto a eliminar")
            self.get_products()

    def modificarProducto(self):
        try:
            id = self.tree.item(self.tree.selection())['values'][0]
            producto = ModificarProducto(self, id, self.win)

        except IndexError as e:
            messagebox.showinfo("","Debe seleccionar un producto a modificar")
            self.get_products()

    def registrarVenta(self):
        try:
            id = self.tree.item(self.tree.selection())['values'][0]
            venta = VentasGui(self, id, self.win)

        except IndexError as e:
            messagebox.showinfo("", "Debe seleccionar un producto para realizar la venta")
            self.get_products()