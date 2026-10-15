
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.color(turtle_colors.pop())
  my_turtles.append(t)

# Starting values X and Y
startx = 0
starty = 0

# Direction of turtle
direction = 90

# Adjusting the starting values for the next turtle
for t in my_turtles:
    t.penup()
    t.goto(startx, starty)
    t.setheading(direction)
    t.right(45)
    t.forward(50)
    t.pendown()

# Change direction to the heading of last turtle
direction = t.heading()

#
    startx = t.xcor()
    starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()