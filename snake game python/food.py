from turtle import Turtle #Importamos la libreria de Turtle para poder funcionar el juego.
import random #Importa la libreria de random para que aparezca un objeto de manera aleatoria por toda la ventana.

class Food(Turtle): 

    def __init__(self): 
        super().__init__() 
        self.shape("circle") #Define la forma del objeto
        self.penup() #No deja rastro del dibujo(la linea).
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) 

        self.color("red") #Cambia el color de la comida.
        self.speed("fastest") #Define la velocidad de reapariión de la comida.
        self.refresh() # Indica que la comida debe reaparecer.

    def refresh(self): 
        random_x = random.randint(-280, 280) #Funciona para ubicar el objeto de la ventana de forma aleatoria en el eje x.
        random_y = random.randint(-280, 280) #Funciona para ubicar el objeto de la ventana de forma aleatoria en el eje y.
        self.goto(random_x, random_y) #Sirve para definir a que direcciones va el objeto.