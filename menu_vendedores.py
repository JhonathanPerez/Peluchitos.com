from tkinter import *
from tkinter import messagebox

from inventario import Inventario
from historial_ventas import HistorialVenta
from ventas import Venta

class Menu:
    def __init__(self, padre):
        self.padre = padre
        self.win = Toplevel(self.padre)
        self.win.title("Menú principal")
        self.win.geometry("500x420")
        self.win.resizable(0, 0)
        self.crearWidgets()
        self.win.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.win.mainloop()

    def destroyWindow(self):
        self.win.withdraw()

    def clearInput(self):
        self.entryOpcion.delete(0,END)

    def obtenerOpcion(self):
        op = self.entryOpcion.get()

        if op == "1":
            self.destroyWindow()
            producto = Inventario(self, self.win)

        elif op == "2":
            venta = Venta()

            if venta.mostrar_ventas():
                self.destroyWindow()
                historial = HistorialVenta(self, self.win)
            else:
                message = "No hay ventas registradas en el sistema"
                self.clearInput()
                messagebox.showwarning("",message)

        else:
            messagebox.showerror(":(", "La opción ingresada no es válida")

    def crearWidgets(self):
        # Creating a Frame Container
        self.frameLogo = Frame(self.win)
        self.frameLogo.pack(fill=BOTH, pady=10)

        self.frameLabels = Frame(self.win)
        self.frameLabels.pack(fill=BOTH)

        self.frameInput = Frame(self.win)
        self.frameInput.pack(fill=BOTH, pady=30)

        self.frameButton = Frame(self.win)
        self.frameButton.pack(fill=BOTH)

        #Create image logo
        self.path = './img/logo.png'
        self.imagen = PhotoImage(file=self.path)
        self.img_label = Label(self.frameLogo, image=self.imagen)
        self.img_label.pack(padx=10, pady=20)

        #Create labels
        self.lblMenu = Label(self.frameLabels, text="Menú principal", font="sans 16 bold")
        self.lblMenu.pack(pady=20)

        self.lblAdicionar = Label(self.frameLabels, text="1.Modificar inventario y realizar ventas")
        self.lblAdicionar.pack()

        self.lblGanancias = Label(self.frameLabels, text="2.Mostrar ventas y ganacias")
        self.lblGanancias.pack()

        #Create entry

        self.lblOpcion = Label(self.frameInput, text="Ingrese su opción: ")
        self.lblOpcion.pack(side="left", padx=50)

        self.entryOpcion = Entry(self.frameInput)
        self.entryOpcion.focus()
        self.entryOpcion.pack()

        # Create Button opción
        self.btnEnviar = Button(self.frameButton,text="Enviar", command=self.obtenerOpcion)
        self.btnEnviar.pack(pady=20)

    def on_closing(self):
        if messagebox.askokcancel("Salir", "Estás seguro que deseas salir?"):
            self.padre.deiconify()
            self.win.destroy()






