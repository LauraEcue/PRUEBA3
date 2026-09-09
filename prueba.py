class usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def imprimir(self):
        print(self.nombre, self.correo)

usuario1 = usuario("Laura", "laura@gmial.com")
usuario2 = usuario("andres", "andres@gmail.com")

usuario1.imprimir()




class Producto:
    pass
producto1 = Producto()
producto2 = Producto()

producto1.nombre = "arroz"
producto1.precio = 5000

print()