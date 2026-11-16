# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
jerry_color = "green"
jerry_size = 2
jerry_shape = "turtle"
score = 0

#-----initialize turtle-----
jerry = trtl.Turtle()
jerry.shape(jerry_shape)
jerry.shapesize(jerry_size)
jerry.fillcolor(jerry_color)

score_writer = trtl.Turtle()

#-----game functions--------
def update_score():
    global score
    score += 1
    print(score)

def jerry_clicked(x,y):
    change_position()
    update_score()

def change_position():
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-150, 150)
    jerry.penup()
    jerry.hideturtle()
    jerry.goto(new_xpos, new_ypos)
    jerry.pendown()
    jerry.showturtle()

#-----events----------------
jerry.onclick(jerry_clicked)

wn=trtl.Screen()
wn.mainloop()