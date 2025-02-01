import sys
import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()
    
    t.getscreen().tracer(0,0)

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    t.getscreen().update()

    window.mainloop()



def main():
    try:
        d = int(sys.argv[1])
    except ValueError:
        print("Помилка: введіть число")
        return

    draw_koch_curve(d)

if __name__ == "__main__":
    main()
