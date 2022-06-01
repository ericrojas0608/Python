import turtle
import time
import random

retraso = 0.1
marcador = 0
marcador_alto = 0

s = turtle.Screen()
s.setup(650,650)
s.bgcolor('gray')
s.title('Proyecto 2')
s.tracer()

snake = turtle.Turtle()
snake.speed(1)
snake.shape('square')
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'
snake.color('green')

comida = turtle.Turtle()
comida.shape('circle')
comida.color('orange')
comida.penup()
comida.goto(0,100)
comida.speed(0)

cuerpo = []

texto = turtle.Turtle()
texto.speed(0)
texto.color('black')
texto.penup()
texto.hideturtle()
texto.goto(0,-260)
texto.write("Marcador: 0\tMarcador mas alto: 0", align="center", font=("Verdana", 24, "normal"))

# Se van a llamar cuando se presionen las teclas
def arriba():
    snake.direction = 'up'

def abajo():
    snake.direction = 'down'

def derecha():
    snake.direction = 'right'

def izquierda():
    snake.direction = 'left'

# Determinar el movimiento de la serpiente
def movimiento():
    if snake.direction == 'up':
        y = snake.ycor() #devuelve la ubicacion en Y
        snake.sety(y + 20) #mueve el objeto en el eje Y

    if snake.direction == 'down':
        y = snake.ycor() #devuelve la ubicacion en Y
        snake.sety(y - 20) #mueve el objeto en el eje Y
    
    if snake.direction == 'right':
        x = snake.xcor() #devuelve la ubicacion en Y
        snake.setx(x + 20) #mueve el objeto en el eje Y
    
    if snake.direction == 'left':
        x = snake.xcor() #devuelve la ubicacion en Y
        snake.setx(x - 20) #mueve el objeto en el eje Y

s.listen()
s.onkeypress(arriba,'Up')
s.onkeypress(abajo, 'Down')
s.onkeypress(izquierda,'Left')
s.onkeypress(derecha,'Right')

while True:
    s.update()

    #cuando toda los bordes
    if snake.xcor() > 300 or snake.xcor() < -300 or snake.ycor() > 300 or snake.ycor() < -300:
        time.sleep(2)

        for i in cuerpo:
            i.clear()
            i.hideturtle()
        
        snake.home()
        snake.direction = 'stop'
        cuerpo.clear()

        marcador = 0
        texto.clear()
        texto.write("Marcador:{}\tMarcador mas alto:{}".format(marcador,marcador_alto),align="center", font=("Verdana",24,"normal"))

    if snake.distance(comida) < 20:
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        comida.goto(x,y)
        
        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape('square')
        nuevo_cuerpo.color('green')
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,100)
        nuevo_cuerpo.speed(0)
        cuerpo.append(nuevo_cuerpo)

        marcador += 10
        if marcador > marcador_alto:
            marcador_alto = marcador
            texto.clear()
            texto.write("Marcador:{}\tMarcador mas alto:{}".format(marcador,marcador_alto), align="center", font=("Verdana",24,"normal"))

    total = len(cuerpo)
    for i in range(total -1, 0, -1):
        x = cuerpo[i-1].xcor()
        y = cuerpo[i-1].ycor()
        cuerpo[i].goto(x,y)

    if total > 0:
        x = snake.xcor()
        y = snake.ycor()
        cuerpo[0].goto(x,y)

    movimiento()

    for i in cuerpo:
        if i.distance(snake) < 20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            snake.home()
            cuerpo.clear()
            snake.direction = 'stop'

    time.sleep(retraso)

turtle.done()