import turtle


class fractalCuadrado:
    def __init__(self, velocidad = 0):
        self.tortuga = turtle.Turtle()
        self.tortuga.speed(velocidad)


    def crearCuadrado(self, longitudDeLado):
        self.tortuga.pensize(2)
        i = 1
        while i <= 4:
            self.tortuga.forward(longitudDeLado)
            self.tortuga.left(90)
            i += 1

    def crearCuadradosConCiclos(self, cantidadDeCuadrados, longitudDeLado, cantidadDeGrados, color):
        self.tortuga.pencolor(color)

        inicial = 1

        while inicial <= cantidadDeCuadrados:
            self.crearCuadrado(longitudDeLado)
            self.tortuga.left(cantidadDeGrados)

            inicial += 1

    def crearCuadradosRecursivo(self, cantidadDeCuadrados, longitudDeCuadrado, cantidadDeGrados, color):
        self.tortuga.pencolor(color)
        if cantidadDeCuadrados < 1:
            return
        else:
            self.crearCuadrado(longitudDeCuadrado)
            self.tortuga.left(cantidadDeGrados)
            self.crearCuadradosRecursivo(cantidadDeCuadrados - 1, longitudDeCuadrado, cantidadDeGrados, color)


        

            

cuadrado1 = fractalCuadrado(0)

cuadrado1.crearCuadrado(150)
cantidadDeGrados =  5
cantidadDeCuadrados = 360/cantidadDeGrados
cuadrado1.crearCuadradosConCiclos(int(cantidadDeCuadrados), 100, cantidadDeGrados, "green")
cuadrado1.crearCuadradosRecursivo(int(cantidadDeCuadrados), 150, cantidadDeGrados, "red") 
cuadrado1.crearCuadradosRecursivo(int(cantidadDeCuadrados), 200, cantidadDeGrados, "blue")
turtle.done()