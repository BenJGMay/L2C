import turtle

def setup(pencil):
    pencil.color('blue')
    pencil.penup()
    pencil.goto(-200, 100)
    pencil.pendown()

def koch(pencil, size, order):
    if order == 0:
        pencil.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(pencil, size/3, order-1)
            pencil.left(angle)

def main(value):
    pencil = turtle.Turtle()
    setup(pencil)

    order = value
    size = 400
    koch(pencil, size, order)

if __name__ == '__main__':
    main(3)
    turtle.tracer(100)
    turtle.mainloop()
