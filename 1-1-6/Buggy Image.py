#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
painter = trtl.Turtle()
painter.pensize(40)


#Draw spider body
painter.circle(20)

#Configure spider legs
legs = 8
draw_legs = 70
space_between_legs = 380 / legs
painter.pensize(5)

#Draw legs
n = 0
while (n < legs):
  painter.goto(0, 20)
  painter.setheading(space_between_legs * n)
  painter.forward(draw_legs)
  n = n + 1

painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()