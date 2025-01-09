import random
import turtle
x = input('Please input your email:')
y = int(input('Please enter the speed (1-20):'))
colors = ['red','cyan','pink' ,'yellow', 'green','orange']
t = turtle.Turtle()
t.speed(y)
turtle.bgcolor("black")
length=100
angle =50
size=5
for i in range(length):
    color=random.choice(colors)
    t.pencolor(color)
    t.fillcolor(color)
    if i < length-1:
        t.penup()
        t.forward(i+50)
        t.pendown()
        t.left(angle)
        t.begin_fill()
        t.circle(size)
        t.end_fill()
    else:
        t.penup()
        t.forward(i+50)
        t.left(angle)
        t.write(x,align="left")
        t.fillcolor('blue')
        
turtle.exitonclick()
turtle.bgcolor("black")
