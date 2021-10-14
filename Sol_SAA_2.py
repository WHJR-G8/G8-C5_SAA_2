import turtle

side = int(input('Enter the side value'))

if 0 < side < 100:
    turtle.fillcolor('red')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.end_fill()
    
elif (100 <= side) <= 200:
    turtle.fillcolor('green')
    (turtle.begin_fill())
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.end_fill()
    
else:
    turtle.fillcolor('blue')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.end_fill()
