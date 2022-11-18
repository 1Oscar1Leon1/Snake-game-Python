from turtle import Turtle #Importamos la libreria para diseñar la serpiente.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] #Es la posición y distancia que lleva de cada segmento.
MOVE_DISTANCE = 20 #Nos define el movimiento del objeto.
UP = 90 # Nos define el giro del objeto hacia arriba.
DOWN = 270 # Nos define el giro del objeto hacia abajo.
LEFT = 180 # Nos define el giro del objeto hacia la izquierda.
RIGHT = 0 # Nos define el giro del objeto hacia la derecha.

class Snake: #Clase en la cual definimos funciones.

    def __init__(self): 
        self.segments = [] # Funciona para guardar cada segmento.
        self.create_snake() # Funciona para crear la serpiente.
        self.head = self.segments[0] # Guarda los dos datos anteriores dentro del objeto.

    def create_snake(self): 
        for position in STARTING_POSITIONS: 
            self.add_segment(position) #Nos define la posición inicial del objeto.

    def add_segment(self, position): #
        new_segment = Turtle("square") #
        new_segment.color("blue") # Podemos cambiar el color de la serpiente.
        new_segment.penup() #No deja rastro del dibujo(la linea).
        new_segment.goto(position) #Define la posición del objeto.
        self.segments.append(new_segment) #Nos agrega lo anterior al objeto(serpiente).

    #Definimos la posición donde añadimos el nuevo segmento del cuerpo de la serpiente.
    def extend(self): 

        self.add_segment(self.segments[-1].position()) #

    #Definimos el cuerpo de la serpiente para que los segmentos se unan y se mantengan en la misma posición.
    def move(self): 
        for seg_num in range(len(self.segments)- 1, 0, -1): 

            new_x = self.segments[seg_num -1].xcor() 

            new_y = self.segments[seg_num -1].ycor() 

            self.segments[seg_num].goto(new_x,new_y) 

        self.head.forward(MOVE_DISTANCE) 

    #Definimos el movimiento del sistema que nos indica la dirección abajo.
    def up(self): 
        if self.head.heading() != DOWN: 
            self.head.setheading(UP) 

    #Definimos el movimiento del sistema que nos indica la dirección arriba.

    def down(self): 
        if self.head.heading() != UP: 
            self.head.setheading(DOWN) 
 
    #Definimos el movimiento del sistema que nos indica la dirección derecha.

    def left(self): 
        if self.head.heading() != RIGHT: 
            self.head.setheading(LEFT) 

    #Definimos el movimiento del sistema que nos indica la dirección izquierda.

    def right(self): 
        if self.head.heading() != LEFT: 
            self.head.setheading(RIGHT) 