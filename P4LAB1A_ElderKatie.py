# turtle graphics
# cti 110

#initialize
import turtle
win = turtle.Screen()

# making turtle
t = turtle.Turtle()
t.shape("turtle")

# Draw a square
for _ in range(4):
    t.forward(100)
    t.left(90)

# Move to a new starting position for the triangle
t.penup()
t.goto(150, 0)
# Move right to separate the shapes
t.pendown()

# Draw a triangle
for _ in range(3):
    t.forward(100)
    t.left(120)

# at the end, keep the window open until closed
win.mainloop()
