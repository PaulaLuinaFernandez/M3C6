class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

usuario_uno = Usuario("Paula", "Password")


print(f'Nombre de usuario: {usuario_uno.nombre_usuario}')
print(f'Contrasena: {usuario_uno.contrasena}')

