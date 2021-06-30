from tkinter import *
from tkinter import messagebox

from peluches import  Producto

class ModificarProducto:
    def __init__(self, padre,idProducto, ventanaPadre):
        self.padre = padre
        self.ventanaPadre = ventanaPadre
        self.idProducto = idProducto
        self.win = Toplevel(self.ventanaPadre)
        self.win.title("Modificar producto")
        self.win.geometry("500x495")
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

        # Create image logo
        self.path = './img/modificar.png'
        self.imagen = PhotoImage(file=self.path)
        self.img_label = Label(self.frameLogo, image=self.imagen)
        self.img_label.pack(padx=10, pady=20)

        self.frameFather = Frame(self.win)
        self.frameFather.pack()

        self.frameFather2 = Frame(self.win)
        self.frameFather2.pack()

        self.frameLabels = Frame(self.frameFather)
        self.frameLabels.pack(side=LEFT, pady=30)

        self.frameOldInputs = Frame(self.frameFather)
        self.frameOldInputs.pack(side=LEFT)

        self.frameLabels2 = Frame(self.frameFather2)
        self.frameLabels2.pack(side=LEFT, pady=30)

        self.frameInputs = Frame(self.frameFather2)
        self.frameInputs.pack(side=LEFT)

        self.frameButtons = Frame(self.win)
        self.frameButtons.pack(pady=20)

        # Labels

        self.lblId = Label(self.frameLabels, text="Identificador: ", font="sans 12")
        self.lblId.pack(side=TOP, padx=20)

        self.lblPrecio = Label(self.frameLabels, text="Precio: ", font="sans 12")
        self.lblPrecio.pack(side="bottom", padx=22)

        self.lblCantidad = Label(self.frameLabels, text="Cantidad: ", font="sans 12")
        self.lblCantidad.pack(side="bottom", padx=22)

        self.lblNombre = Label(self.frameLabels, text="Nombre: ", font="sans 12")
        self.lblNombre.pack(side="bottom", padx=22)

        # Inputs
        producto = Producto()
        item = producto.obtenerProducto(self.idProducto)

        self.entryOldId = Entry(self.frameOldInputs, textvariable = StringVar(value = item.id), state = 'readonly')
        self.entryOldId.pack()

        self.entryOldNombre = Entry(self.frameOldInputs, textvariable = StringVar(value = item.nombre), state = 'readonly')
        self.entryOldNombre.pack(pady=2)

        self.entryOldCantidad = Entry(self.frameOldInputs, textvariable = StringVar(value = item.cantidad), state = 'readonly')
        self.entryOldCantidad.pack(pady=2)

        self.entryOldPrecio = Entry(self.frameOldInputs, textvariable = StringVar(value = item.precio), state = 'readonly')
        self.entryOldPrecio.pack()

        ########################################
        self.lblPrecio = Label(self.frameLabels2, text="Precio: ", font="sans 12")
        self.lblPrecio.pack(side="bottom", padx=22)

        self.lblCantidad = Label(self.frameLabels2, text="Cantidad: ", font="sans 12")
        self.lblCantidad.pack(side="bottom", padx=22)

        self.lblNombre = Label(self.frameLabels2, text="Nombre: ", font="sans 12")
        self.lblNombre.pack(side="bottom", padx=22)

        #############################################3

        self.entryNombre = Entry(self.frameInputs)
        self.entryNombre.pack(pady=2)

        self.entryCantidad = Entry(self.frameInputs)
        self.entryCantidad.pack(pady=2)

        self.entryPrecio = Entry(self.frameInputs)
        self.entryPrecio.pack()

        # Buttons
        self.buttonAgregar = Button(self.frameButtons, text='Modificar',command=self.modificar).pack(side=LEFT,padx=20)
        self.buttonCancelar = Button(self.frameButtons, text='Cancelar', command=self.destroyWindow).pack(side=LEFT)

    def modificar(self):
        try:
            id = self.idProducto
            nombre = self.entryNombre.get()
            cantidad = int(self.entryCantidad.get())
            precio = int(self.entryPrecio.get())

            producto = Producto(id, nombre, cantidad, precio)

            if producto.modificar_producto(producto):
                message = "El producto se modificó exitosamente"
                messagebox.showinfo("", message)
                self.padre.get_products()
                self.win.destroy()

            else:
                message = "Ocurrió un error al modificar el producto :("
                messagebox.showinfo("", message)
                self.destroyWindow()

        except ValueError:
            message = "Se ingresó algún dato de forma incorrecta o campos vacios"
            messagebox.showerror(":(", message)








