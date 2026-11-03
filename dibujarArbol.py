import turtle

class Arbol:
    def __init__(self, velocidad = 0):
        self.tortuga = turtle.Turtle()
        self.tortuga.speed(velocidad)
        self.tortuga.left(90)

    def dibujarNivelRecursivo(self, longitud, cantidadDeNiveles):
        self.tortuga.pensize(cantidadDeNiveles * 2)
        if cantidadDeNiveles <= 3:
            self.tortuga.pencolor("green")
        else:
            self.tortuga.pencolor("brown")
        if cantidadDeNiveles < 1:
            return
        else:
            self.tortuga.forward(longitud)
            self.tortuga.left(30)
            self.dibujarNivelRecursivo(longitud * 0.7, cantidadDeNiveles - 1)
            self.tortuga.right(60)
            self.dibujarNivelRecursivo(longitud * 0.7, cantidadDeNiveles - 1)
            self.tortuga.left(30)
            self.tortuga.forward(-longitud)



Rama1 = Arbol(5)

Rama1.dibujarNivelRecursivo(100, 6)
turtle.done()