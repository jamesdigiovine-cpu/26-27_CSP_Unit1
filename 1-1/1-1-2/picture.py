# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()


painter.fillcolor("Blue")
painter.begin_fill()
painter.circle(150)
painter.end_fill()

painter.penup()
painter.goto(300, 0)
painter.pendown()

painter.fillcolor("Yellow")
painter.begin_fill()
painter.circle(150)
painter.end_fill()

painter.penup()
painter.goto(-300, 0)
painter.pendown()

painter.fillcolor("Red")
painter.begin_fill()
painter.circle(150)
painter.end_fill()

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()