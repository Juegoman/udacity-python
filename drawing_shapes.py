import turtle

def draw_square(t):
    i = 0
    while i < 4:
        t.forward(100)
        t.right(90)
        i += 1
def draw_circle_with_squares(t):
    j = 0
    while j < 36:
        draw_square(t)
        t.right(10)
        j += 1
# def draw_circle():
#     tort = turtle.Turtle()
#     tort.shape("triangle")
#     tort.color("green")
#     tort.speed(2)
#
#     tort.circle(50)
# def draw_triangle():
#     tart = turtle.Turtle()
#     tart.color("red")
#
#     tart.right(180)
#     i = 0
#     while i < 3:
#         tart.forward(100)
#         tart.left(120)
#         i += 1
window = turtle.Screen()
window.bgcolor("grey")

turt = turtle.Turtle()
turt.shape("arrow")
turt.color("blue")
turt.speed(7)

draw_circle_with_squares(turt)
#draw_square()
#draw_circle()
#draw_triangle()

window.exitonclick()
