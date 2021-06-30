from tkinter import *
from tkinter import messagebox

from productos import Producto
from usuarios import Usuario
from menu_vendedores import Menu

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("450x390")
        self.root.resizable(0, 0)
        self.crearWidgets()

    def destroyWindow(self):
        self.root.withdraw()

    def clearInput(self):
        self.entryUser.delete(0,END)
        self.entryPassword.delete(0,END)

    def login(self):
        self.nombreUsuario = self.entryUser.get()
        self.contrasena = self.entryPassword.get()

        self.usuario = Usuario(nombreUsuario=self.nombreUsuario, contrasena=self.contrasena)
        self.usuario.agregarAdmin()

        if self.usuario.validarUsuario():
            self.destroyWindow()
            menuVendedores = Menu(self.root)
        else:
            titulo = ":("
            mensaje = "Los datos ingresados no son validos, intente nuevamente"
            messagebox.showerror(titulo, mensaje)
            self.clearInput()
            self.entryUser.focus()


    def crearWidgets(self):
        # Creating a Frame Container
        self.frameLogo = Frame(self.root)
        self.frameLogo.pack(fill=BOTH, pady=10)

        self.frameInputs = Frame(self.root)
        self.frameInputs.pack(fill=BOTH, pady=5)

        self.frameInputs2 = Frame(self.root)
        self.frameInputs2.pack(fill=BOTH)

        # #Create image logo
        self.path = './img/logo.png'
        self.imagen = PhotoImage(file=self.path)
        self.img_label = Label(self.frameLogo, image=self.imagen)
        self.img_label.pack(padx=10,pady=20)

        #Create label login
        self.lblLogin = Label(self.frameLogo, text="Login", font="sans 14")
        self.lblLogin.pack(pady=15)

        #Create label username and entry
        self.lblUser = Label(self.frameInputs, text="Username: ", font="sans 14")
        self.lblUser.pack(side="left", padx=20)

        self.entryUser = Entry(self.frameInputs)
        self.entryUser.focus()
        self.entryUser.pack()

        #Create label password and entry
        self.lblPassword = Label(self.frameInputs2, text="Password: ", font="sans 14")
        self.lblPassword.pack(side="left", padx=22)

        self.entryPassword = Entry(self.frameInputs2, show="*")
        self.entryPassword.pack()

        #Create Button login
        self.btnLogin = Button(text="Ingresar", command=self.login)
        self.btnLogin.pack(pady=20)

        #Create label credits
        self.lblCredits = Label(text="Designed by: @Jperez_ortega")
        self.lblCredits.pack(side=BOTTOM)

if __name__ == '__main__':
    root = Tk()
    window = Login(root)
    root.mainloop()
