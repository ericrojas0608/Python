import turtle

s=turtle.Screen()
t=turtle.Turtle()

#color de fondo del lienzo
s.bgcolor("green")

#modificar nombre del lienzo
s.title("Proyecto 1")

#modificar el tamaño de la tortuga
t.shapesize(10,5,1)
t.shapesize(5,10,1)
t.shapesize(3,3,3)

#cambiar color de la tortuga
t.fillcolor("orange")
t.forward(100)

#cambiar color de la tinta
t.pencolor("white")
t.forward(100)

#cambiar grosor de la linea
t.pensize(5)
t.forward(100)

turtle.done()