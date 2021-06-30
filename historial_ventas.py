from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from ventas import Venta


class HistorialVenta:
    def __init__(self, padre, ventanaPadre):
        self.padre = padre
        self.ventanaPadre = ventanaPadre
        self.win = Toplevel(self.ventanaPadre)
        self.win.title("Historial de ventas")
        self.win.geometry("900x500")
        self.win.resizable(0, 0)
        self.crearWidgets()
        self.get_ventas()
        self.win.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.win.mainloop()

    venta = Venta()

    def destroyWindow(self):
        self.ventanaPadre.deiconify()
        self.padre.clearInput()
        self.win.destroy()

    def crearWidgets(self):
        # Creating a Frames

        self.frameLogo = Frame(self.win)
        self.frameLogo.pack(fill=BOTH, pady=10)

        self.frameTreeView = Frame(self.win)
        self.frameTreeView.pack(fill=BOTH, pady=10)

        self.frameLabels = Frame(self.win)
        self.frameLabels.pack(fill=BOTH, pady=10)

        self.frameButton = Frame(self.win)
        self.frameButton.pack(fill=BOTH, pady=10)

        # Create image logo
        self.path = './img/historial_ventas.png'
        self.imagen = PhotoImage(file=self.path)
        self.img_label = Label(self.frameLogo, image=self.imagen)
        self.img_label.pack(padx=10, pady=20)

        # Table
        self.tree = ttk.Treeview(self.frameTreeView)
        self.tree['columns'] = ('Id', 'Id_producto', 'Nombre_producto', 'Unidades', 'Valor', 'Fecha')
        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('Id', anchor=CENTER, width=80)
        self.tree.column('Id_producto', anchor=CENTER, width=100)
        self.tree.column('Nombre_producto', anchor=CENTER, width=100)
        self.tree.column('Unidades', anchor=CENTER, width=80)
        self.tree.column('Valor', anchor=CENTER, width=80)
        self.tree.column('Fecha', anchor=CENTER, width=80)

        self.tree.heading('#0', text='', anchor=CENTER)
        self.tree.heading('Id', text='Id', anchor=CENTER)
        self.tree.heading('Id_producto', text='Id_producto', anchor=CENTER)
        self.tree.heading('Nombre_producto', text='Nombre_producto', anchor=CENTER)
        self.tree.heading('Unidades', text='Unidades', anchor=CENTER)
        self.tree.heading('Valor', text='Valor', anchor=CENTER)
        self.tree.heading('Fecha', text='Fecha', anchor=CENTER)

        self.tree.pack(fill=X)

        valor_total, total_ventas = self.venta.calcular_total_ventas()

        message = f'Se han registrado {total_ventas} ventas para un valor total de ${valor_total} COP'
        self.lblGanacias = Label(self.frameLabels, text=message)
        self.lblGanacias.pack()

        self.btnCerrar = Button(self.frameButton, text="Cerrar", command=self.destroyWindow)
        self.btnCerrar.pack(pady=20)

    # Get ventas from the list

    def get_ventas(self):
        # cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        # getting data
        ventas = self.venta.get_ventas()

        for venta in ventas:
            self.tree.insert('', 0, text='',values=(venta.id_venta, venta.id_producto, venta.nombre_producto, venta.unidades, venta.valor, venta.fecha))

    def on_closing(self):
        if messagebox.askokcancel("Salir", "Estás seguro que deseas salir?"):
            self.ventanaPadre.deiconify()
            self.padre.clearInput()
            self.win.destroy()



