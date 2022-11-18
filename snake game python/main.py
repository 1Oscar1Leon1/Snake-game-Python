from turtle import Screen #Se Importa la libreria llamada Turtle.
from snake import Snake #Llama el archivo Snake y importa la clase Snake. 
from food import Food # Llama el archivo Food y importa la clase Food.
from scoreboard import Scoreboard # Llama el archivo scoreboard y importa la clase scoreboard.
import time # Nos permite contar el tiempo desde la ejecución y nos permite controlar el flujo del tiempo.

#Creación de la ventana
screen = Screen() # Importamos la ventana 
screen.setup(width=600, height=600) #Controla las dimensiones de la ventana. 
screen.bgcolor("yellowgreen") #Cambia de color del fondo de la ventana.
screen.title("My Snake Game") #Nombra el titulo de que llevara la ventana.
screen.tracer(0) #Reonoce la animación de la libreria de Turtle.

snake = Snake() #Importa la clase Snake.
food = Food() #Importa la clase Food.
scoreboard = Scoreboard() #Importa la clase scoreboard.

screen.listen() #Especifica el número de conexiones no aceptadas que el sistema permitirá antes de rechazar nuevas conexiones.  
screen.onkey(snake.up, "Up") #Vincula el evento de liberación de la tecla superior.
screen.onkey(snake.down, "Down") #Vincula el evento de liberación de la tecla inferior.
screen.onkey(snake.left, "Left") #Vincula el evento de liberación de la tecla izquierda.
screen.onkey(snake.right, "Right") #Vincula el evento de liberación de la tecla derecha.

game_is_on = True #Se crea un segmento que es verdadero.
while game_is_on: #Se crea un ciclo para el movimiento.
    screen.update() #Inserta elementos especificos de una libreria.

    time.sleep(0.1) #Controla la velocidad de la serpiente.
    snake.move() # Detecta el moviminet de la serpiente.

    #Detect collision with food.
    if snake.head.distance(food) < 15: #
        food.refresh() # Vuelve a crear el elemento de la comida.
        snake.extend() # Consume la comida.
        scoreboard.increase_score() # Al consumir la comida el puntaje va en aumento en una sola unidad. 

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280: #
        game_is_on = False #
        scoreboard.game_over() #Termina el juego cuando detecta que hubo una colision en una cara de la ventana.

    #Detect collision with tail.
    for segment in snake.segments: #
        if segment == snake.head: #
            pass #
        elif snake.head.distance(segment) < 10: #
            game_is_on = False #
            scoreboard.game_over() #Termina el juego cuando detecta que hubo una colision en una parte del cuerpo de la serpiente.

screen.exitonclick() #