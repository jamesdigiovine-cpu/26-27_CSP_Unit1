import turtle as trtl

painter = trtl.Turtle()

painter.fillcolor("yellow")
painter.begin_fill()
painter.circle(100)
painter.end_fill()

painter.penup()
painter.goto(0, 50)
painter.pendown()


painter.fillcolor("white")
painter.begin_fill()
painter.circle(50)
painter.end_fill()


painter.penup()
painter.goto(0, 200)
painter.pendown()

painter.fillcolor("yellow")
painter.begin_fill()
painter.circle(100)
painter.end_fill()

painter.penup()
painter.goto(0, 250)
painter.pendown()


painter.fillcolor("white")
painter.begin_fill()
painter.circle(50)
painter.end_fill()



wn = trtl.Screen()
wn.mainloop()