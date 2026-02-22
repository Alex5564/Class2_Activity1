import turtle

Screen=turtle.Screen()
Screen.bgcolor("blue")
Screen.setup(300,400)


t=turtle.Turtle()

for i in range(5):
 t.penup()
 t.forward(150)
 t.right(144)

 t.pendown()
 t.right(144)


turtle.done()
