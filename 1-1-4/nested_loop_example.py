import turtle as trtl

# Define the color values
color1 = "blue"
color2 = "yellow"

# Define the screen
wn = trtl.Screen()
width = 400
height = 300

# Define the turtle
painter = trtl.Turtle()
# Make the turtle fast
painter.speed(0)
painter.color(color1)

# Start assuming we will draw
answer = "y"
while (answer == "y"):
    # Loop until the user is bored
    wn.clearscreen()
    # Start in the middle
    painter.goto(0, 0)
    # Setup the space counter
    space = 1

    # Inputing the angle
    angle = int(input("angle:"))
    seg = int(360 / angle)

    while painter.ycor() < height:
        if space % 100 == 0:
            painter.fillcolor(color1)
            painter.color(color1)

        if space % 200 == 0:
            painter.fillcolor(color2)
            painter.color(color2)

        painter.right(angle)
        painter.forward(2 * space + 10)  # experiment
        painter.begin_fill()
        painter.circle(3)
        painter.end_fill()
        space = space + 1

    answer = input("again?")

wn.bye()