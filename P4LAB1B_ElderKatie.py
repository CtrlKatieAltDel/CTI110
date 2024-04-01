import turtle

# Create a screen
wn = turtle.Screen()
import turtle

# Create a turtle
t = turtle.Turtle()
t.shape("turtle")

# Customize the turtle
t.color("pink")    # Set color to pink
t.pensize(5)       # Set pen size

# Draw the letter K
t.penup()
t.goto(-150, 0)
t.pendown()
t.left(90)
t.forward(100)
t.backward(50)
t.right(45)
t.forward(70)
t.backward(70)
t.right(90)
t.forward(70)

# Raise the pen and move to draw the letter E
t.penup()
t.goto(-50, 0)
t.pendown()

# Customize the turtle
t.color("pink")    # Set color to pink
t.pensize(5)       # Set pen size

# Draw the letter E
t.left(90)
t.forward(100)
t.backward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.backward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)

# Keep the window open until manually closed
wn.mainloop()
