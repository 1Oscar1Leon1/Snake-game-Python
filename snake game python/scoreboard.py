from turtle import Turtle #Importamos la libreria de Turtle para hacer el sistema de puntaje.
ALIGNMENT = "center" #Define la ubicación
FONT = ("arial", 24, "normal") # Estilo de las letras y tamaño

class Scoreboard(Turtle): #Clase en la cual definimos funciones. 

    def __init__(self): 
        super().__init__() 
        self.score = 0 #Define un valor absoluto 
        self.color("white") #Color del texto que aparece en ventana.
        self.penup() #No deja rastro del dibujo(la linea).
        self.goto(0, 270) # Define la ubicación del texto.
        self.hideturtle() #Su función es hacer que el objeto sea invicible.
        self.update_scoreboard() #Actializa un nuevo dato

    def update_scoreboard(self): 
        self.write(f"Score: {self.score}",align=ALIGNMENT, font=FONT) #Muestra el texto "SCORE"

    def game_over(self): 
        self.goto(0, 0) #Ubicaion del Tesxo
        self.write("GAME OVER",align=ALIGNMENT, font=FONT) #Muestra el texto "GAME OVER"

    def increase_score(self): #Funcionamiento de la tabla de puntaje.
        self.score += 1 #Incrementa el puntaje a una unidad.
        self.clear() #Limpia el Puntaje anterior.
        self.update_scoreboard() #Actualiza el puntaje.