class Usuario:
    """ Representa un usuario en chat UNINTEP """
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo


    def enviar_mensaje(self, mensaje):
        """ Envia un mensaje a otro usuario """
    

    def consultar_perfil(self, perfil):
        """ Consulta y retorna la información del usuario """
        

usuario_1 = Usuario("ana", "ana@gmail.com")
usuario_2 = Usuario("luis", "luis@gmail.com")
usuario_3 = Usuario("laura", "laura@gmail.com")

print (usuario_1.enviar_mensaje.__doc__)

