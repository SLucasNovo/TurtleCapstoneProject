from turtle import Turtle
MOVEMENT_SPEED = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape_turtle()

    def shape_turtle(self):
        self.penup()
        self.hideturtle()
        self.color("green")
        self.shape('turtle')
        self.goto(0, -280)
        self.setheading(90)
        self.showturtle()

    def move(self):
        new_y = self.ycor() + MOVEMENT_SPEED
        self.goto(self.xcor(), new_y)




