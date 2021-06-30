from tkinter import *
from tkinter import messagebox

from productos import Producto


class AnadirProducto():
    def __init__(self, padre, ventanaPadre):
        self.padre = padre
        self.ventanaPadre = ventanaPadre
        self.win = Toplevel(self.ventanaPadre)
        self.win.title("Añadir producto")
        self.win.geometry("500x380")
        self.win.resizable(0, 0)
        # self.win.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.crearWidgets()
        self.win.mainloop()

    def destroyWindow(self):
        self.win.destroy()

    def crearWidgets(self):
        # Creating a Frame Container
        self.frameLogo = Frame(self.win)
        self.frameLogo.pack(pady=10)

        self.frameFather = Frame(self.win)
        self.frameFather.pack()

        self.frameLabels = Frame(self.frameFather)
        self.frameLabels.pack(side=LEFT, pady=30)

        self.frameInputs = Frame(self.frameFather)
        self.frameInputs.pack(side=LEFT)

        self.frameButtons = Frame(self.win)
        self.frameButtons.pack(pady=20)

        # Create image logo
        self.path = './img/anadir.png'
        self.imagen = PhotoImage(file=self.path)
        self.img_label = Label(self.frameLogo, image=self.imagen)
        self.img_label.pack(padx=10, pady=20)


        #Labels
        self.lblId = Label(self.frameLabels, text="Identificador: ", font="sans 12")
        self.lblId.pack(side=TOP, padx=20)

        self.lblPrecio = Label(self.frameLabels, text="Precio: ", font="sans 12")
        self.lblPrecio.pack(side="bottom", padx=22)

        self.lblCantidad = Label(self.frameLabels, text="Cantidad: ", font="sans 12")
        self.lblCantidad.pack(side="bottom", padx=22)

        self.lblNombre = Label(self.frameLabels, text="Nombre: ", font="sans 12")
        self.lblNombre.pack(side="bottom", padx=22)

        #Inputs
        self.entryId = Entry(self.frameInputs)
        self.entryId.focus()
        self.entryId.pack()

        self.entryNombre = Entry(self.frameInputs)
        self.entryNombre.pack(pady=2)

        self.entryCantidad = Entry(self.frameInputs)
        self.entryCantidad.pack(pady=2)

        self.entryPrecio = Entry(self.frameInputs)
        self.entryPrecio.pack()

        #Buttons
        self.buttonAgregar = Button(self.frameButtons, text='Añadir', command=self.agregarProducto).pack(side=LEFT,padx=20)
        self.buttonCancelar = Button(self.frameButtons, text='Cancelar', command=self.destroyWindow).pack(side=LEFT)

    def agregarProducto(self):
        try:
            id = int(self.entryId.get())
            nombre = self.entryNombre.get()
            cantidad = int(self.entryCantidad.get())
            precio = int(self.entryPrecio.get())

            producto = Producto(id, nombre, cantidad, precio)

            if not producto.validarProducto():
                producto.agregarProductos(producto)
                message = "El producto se agregó correctamente"
                self.destroyWindow()
                self.padre.get_products()
                self.padre.cambiarEstadoBotones()
                messagebox.showinfo(":)", message)
            else:
                message = f"El producto con identidicador {id} ya existe"
                messagebox.showerror(":(", message)

        except ValueError:
            message = "Se ingresó algún dato de forma incorrecta o campos vacios"
            messagebox.showerror(":(", message)



