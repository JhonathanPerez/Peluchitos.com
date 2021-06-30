class Usuario:
    def __init__(self, nombreUsuario=None, contrasena=None, rol=None):
        self.nombreUsuario = nombreUsuario
        self.contrasena = contrasena
        self.rol = rol

    listaUsuarios = []

    def agregarAdmin(self):
        usuario = Usuario(nombreUsuario="admin",contrasena="1234",rol="administrador")
        self.listaUsuarios.append(usuario)
        return True


    def validarUsuario(self):
        for usuario in self.listaUsuarios:
            if usuario.nombreUsuario == self.nombreUsuario and usuario.contrasena == self.contrasena:
                return True
        return False

    def mostrarUsuarios(self):
        for usuario in self.listaUsuarios:
            print(usuario.nombreUsuario, usuario.contrasena, usuario.rol)