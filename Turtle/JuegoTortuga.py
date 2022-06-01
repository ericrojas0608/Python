from sys import _enablelegacywindowsfsencoding
import turtle
import random

#crear pantalla
s = turtle.Screen()
s.title("Primer Proyecto")
#personalizar pantalla
s.bgcolor("gray")

#2 jugadores crear los objetos
ply1 = turtle.Turtle()
ply2 = turtle.Turtle()

#modificar las formas
ply1.shape("turtle")
ply1.color("green","green")
ply1.shapesize(2,2,2)
ply1.pensize(3)

ply2.shape("turtle")
ply2.color("blue","blue")
ply2.shapesize(2,2,2)
ply2.pensize(3)

#iniciar la carrera jugador1
ply1.hideturtle()
ply2.hideturtle()

ply1.penup() #no va a dibujar
ply1.goto(250,200)
ply1.pendown() #dibujar con la tortuga
ply1.circle(40)

ply1.penup()
ply1.goto(-250,225)
ply1.showturtle()

#iniciar la carrera jugador2
ply2.penup()
ply2.goto(250,-200)
ply2.pendown()
ply2.circle(40)

ply2.penup()
ply2.goto(-250,-175)
ply2.showturtle()

dado = [1,2,3,4,5,6]

for i in range(20):
    if ply1.pos() >= (200,200):
        print("La tortuga verde ganó ...")
        break
    elif ply2.pos() >= (200,200):
        print("La tortua azul ganó ...")
        break
    else:
        turno1 = input("Presiona la tecla enter para avanzar la tortuga verde ....")
        turno1 = random.choice(dado)
        print("Tu numero es: ", turno1,"\nAvanzas: ", turno1*20)
        ply1.pendown() #lapicero
        ply1.fd(20*turno1)
    
        turno2 = input("Presiona la tecla enter para avanzar la tortuga azul ....")
        turno2 = random.choice(dado)
        print("Tu numero es: ", turno2,"\nAvanzas: ", turno2*20)
        ply2.pendown() #lapicero
        ply2.fd(20*turno2)
   

turtle.done()