import turtle
def draw_square():
    window=turtle.Screen()
    window.bgcolor("red")
    brad=turtle.Turtle()

    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(4)
    brad=turtle.Turtle()
    x=1
    while x<5:
        brad.forward(100)
        brad.right(90)
        x+=1
def draw_circle():
    angie=turtle.Turtle()
    angie.circle(100)
    angie.color("blue")
    angie.shape("arrow")
def draw_triangle():
    tri=turtle.Turtle()
    tri.shape("arrow")
    x=1
    while x<4:
        tri.back(100)
        tri.left(120)
        x+=1
    
draw_square()
draw_circle()
draw_triangle()
