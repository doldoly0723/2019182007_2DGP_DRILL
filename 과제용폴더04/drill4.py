import turtle

x=500
y=100

turtle.penup()
turtle.goto(x,y)
turtle.pendown()
turtle.left(180)


count = 5
while ( count > 0 ):
    cnt = 5
    while( cnt > 0):
        turtle.forward(100); turtle.left(90)
        turtle.forward(100); turtle.left(90)
        turtle.forward(100); turtle.left(90)
        turtle.forward(100); turtle.left(90)
        turtle.penup()
        turtle.forward(100)
        turtle.pendown()
        cnt-=1
    turtle.penup()
    x=500
    y+=100
    turtle.goto(x,y,)
    turtle.pendown()
    count-=1


        
        
