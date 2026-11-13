# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
jerry_color = "green"
jerry_size = 2
jerry_shape = "turtle"

#-----initialize turtle-----
jerry = trtl.Turtle()
jerry.shape(jerry_shape)
jerry.shapesize(jerry_size)
jerry.fillcolor(jerry_color)

#-----game functions--------
def jerry_clicked(x,y):
    print("clicked!")



#-----events----------------
jerry.onclick(jerry_clicked)

wn=trtl.Screen()
wn.mainloop()