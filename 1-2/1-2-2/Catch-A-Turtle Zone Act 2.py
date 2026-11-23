# a121_catch_a_turtle.py
#-----import statements-----
import turtle
import turtle as trtl
import random as rand
import leaderboard as lb

#-----game configuration----
jerry_color = "green"
jerry_size = 2
jerry_shape = "turtle"
score = 0
font_setup = ("Arial", 20, "normal")
list_color = ["red", "orange", "yellow", "blue"]

#-----countdown variables-----
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----leaderboard variables-----
leaderboard_file)name = "a122_leaderboard.txt"
player_name = input("What is Your Name?")


#-----initialize turtle-----
jerry = trtl.Turtle()
jerry.shape(jerry_shape)
jerry.shapesize(jerry_size)
jerry.fillcolor(jerry_color)

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-200, 200)
score_writer.pendown()

#-----countdown writer-----
counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(200, 200)
counter.pendown()

#-----game functions--------
def update_score():
    global score
    score += 1
    print(score)
    score_writer.clear()
    score_writer.write(f"Score: {score}")

def jerry_clicked(x,y):
    global timer, timer_up
    if timer_up == False:
        change_position()
        update_score()
    else:
        jerry.hideturtle()

def change_position():
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-150, 150)
    jerry.penup()
    jerry.hideturtle()
    jerry.goto(new_xpos, new_ypos)
    jerry.pendown()
    jerry.showturtle()

def change_color():
    global list_color
    new_color = rand.choice(list_color)
    turtle.color(new_color)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

#-----events----------------
jerry.onclick(jerry_clicked)

wn=trtl.Screen()
wn.bgcolor("blue")
wn.ontimer(countdown, counter_interval)
wn.mainloop()