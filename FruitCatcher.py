# Welcome to Fruit Catcher

# Game screen
import turtle as trtl
import random
screen = trtl.Screen()
screen.title("Fruit Catcher")
screen.bgcolor("black")
screen.setup(width=750, height=750)

# Background image
bg_image = "1.1.9\FruitBackground.gif"
trtl.bgpic(bg_image)

# Apple turtle
Apple_Image = ("1.1.9\Apple.gif")
screen.addshape(Apple_Image)
apple = trtl.Turtle()
apple.shape(Apple_Image)
apple.color("red")
apple.shapesize(.5)
apple.speed(0)
apple.penup()
apple.goto(random.randint(-250, 250), 250)

# Orange turtle
Orange_Image = ("1.1.9\Orange.gif")
screen.addshape(Orange_Image)
orange = trtl.Turtle()
orange.shape(Orange_Image)
orange.color("orange")
orange.shapesize(1)
orange.speed(0)
orange.penup()
orange.goto(random.randint(-250, 250), 250)

# Lemon turtle
Lemon_Image = ("1.1.9\Lemon.gif")
screen.addshape(Lemon_Image)
lemon = trtl.Turtle()
lemon.shape(Lemon_Image)
lemon.color("yellow")
lemon.shapesize(1.5)
lemon.speed(0)
lemon.penup()
lemon.goto(random.randint(-250, 250), 250)

# Basket turtle
Basket_Image = ("1.1.9\Basket.gif")
screen.addshape(Basket_Image)
basket = trtl.Turtle()
basket.shape(Basket_Image)
basket.color("#b09168")
basket.penup()
basket.goto(0,-275)
basket_speed = 15

# Keybind to move the basket left
def move_left():
    x = basket.xcor()
    x -= basket_speed
    if x < -300:
        x = -300
    basket.setx(x)

# Keybind to move the basket right
def move_right():
    x = basket.xcor()
    x += basket_speed
    if x > 300:
        x = 300
    basket.setx(x)

# Keyboard bindings for basket
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Score
score = 0

# Scoreboard
points = trtl.Turtle()
points.hideturtle()
points.color("black")
points.penup()
points.goto(0, 250)
points.write("Points: 0", align = "center", font =("Courier", 24, "normal"))

# Rules
rules = trtl.Turtle()
rules.hideturtle()
rules.color("black")
rules.penup()
rules.goto(0, 300)
rules.write("Here are the rules to Fruit Catcher! Lemons = -1 point, Oranges = 1 point, Apples = 2 points", align = "center", font = ("Courier", 10, "normal"))

# Define collision
def collision(t1, t2):
    distance = t1.distance(t2)
    if distance < 20:
        return True
    else:
        return False

# Main game loop
while True:
    apple.sety(apple.ycor()-20)
    orange.sety(orange.ycor()-20)
    lemon.sety(lemon.ycor()-20)

    # Check for fruit caught
    if collision(basket, apple):
        apple.goto(random.randint(-250, 250), 250)
        score += 2
        points.clear()
        points.write("Points: " + str(score), align = "center", font = ("Courier", 24, "normal"))
    if collision(basket, orange):
        orange.goto(random.randint(-250, 250), 250)
        score += 1
        points.clear()
        points.write("Points: " + str(score), align = "center", font = ("Courier", 24, "normal"))
    if collision(basket, lemon):
        lemon.goto(random.randint(-250, 250), 250)
        score -= 1
        points.clear()
        points.write("Points: " + str(score), align = "center", font = ("Courier", 24, "normal"))
    
    # Check if the fruit has reached the bottom
    if apple.ycor() < -250:
        apple.goto(random.randint(-250, 250), 250)
    if orange.ycor() < -250:
        orange.goto(random.randint(-250, 250), 250)
    if lemon.ycor() < -250:
        lemon.goto(random.randint(-250, 250), 250)

screen = trtl.Screen()
screen.mainloop()