import turtle as t
import random

def main():
    t.colormode(255)
    painter = t.Turtle()
    painter.speed("fastest")
    painter.penup()
    painter.hideturtle()
    color_list = [(212, 154, 97), (52, 108, 132), (178, 78, 33), (198, 143, 34), (123, 80, 97), (235, 240, 244), (116, 155, 171), (124, 175, 158), (228, 197, 129), (194, 85, 105), (54, 38, 20), (12, 51, 65), (189, 123, 142), (54, 120, 115), (41, 169, 126), (167, 21, 31), (225, 94, 78), (4, 30, 28), (39, 32, 34), (243, 163, 159), (81, 148, 168), (164, 27, 22), (239, 163, 167), (104, 123, 159), (164, 209, 193), (21, 81, 93), (29, 85, 81)]

    paint(painter, color_list, 100)

    window = t.Screen()
    window.exitonclick()

 
def paint(pencil, colors, dots_to_draw):
    pencil.setheading(225)
    pencil.fd(300)
    pencil.setheading(0)

    for dot_count in range(1, dots_to_draw + 1):
        pencil.dot(20, random.choice(colors))
        pencil.penup()
        pencil.forward(50)
        pencil.pendown()
        if dot_count % 10 == 0:
            pencil.penup()
            pencil.setheading(90)
            pencil.forward(50)
            pencil.setheading(180)
            pencil.forward(500)
            pencil.setheading(0)
    




if __name__ == "__main__":
    main()
