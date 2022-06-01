import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.circle(10)
t.speed(10)
t.circle(25)
t.speed(10)
t.circle(50)
t.speed(10)
t.circle(75)
t.speed(10)
t.circle(100)
t.dot(30)  #punto
t.setx(100)
t.sety(-100)

#ocultar la totuga
t.hideturtle

#mostrar la tortuga
t.showturtle

turtle.done()