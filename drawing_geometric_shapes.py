from turtle import Turtle,Screen
turtle=Turtle()
def draw():
    nombre_angle=3
    while nombre_angle<11:
        angle=360/nombre_angle
        for x in range(nombre_angle):
            turtle.forward(100)
            turtle.left(angle)
        nombre_angle+=1
        screen.update()
    turtle.hideturtle()
screen=Screen()
draw()
screen.exitonclick()