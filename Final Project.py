import turtle
import random

wn = turtle.Screen()
wn.title("our game name")
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0)

# player
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"

# list of burgers
burgers = []

# add burgers
for _ in range(20):
    burger = turtle.Turtle()
    burger.speed(0)
    burger.shape("circle")
    burger.color("blue")
    burger.penup()
    burger.goto(0, 250)
    burger.speed = random.randint(1, 4)
    burgers.append(burger)


# functions
def go_left():
    player.direction = "left"


def go_right():
    player.direction = "right"


# keyboard binding (listening to keyboard)
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# main game loop
while True:

    # update screen
    wn.update()

    # player moving
    if player.direction == "left":
        x = player.xcor()
        x -= 3
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += 3
        player.setx(x)

    # moving burgers
    for burger in burgers:
        y = burger.ycor()
        y -= burger.speed
        burger.sety(y)

        # check for off-screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            burger.goto(x, y)

        # check for collision
        if burger.distance(player) < 20:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            burger.goto(x, y)

wn.mainloop()
