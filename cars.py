##### Create cars - random creation moving at a fixed speed

from turtle import Turtle
import random
QUANTITY = 20
COLOR = ['black', 'orange', 'yellow', 'blue', 'red', 'green']
BEGGINING_POSITION_X = 290
BEGGINING_POSITION_Y = 220



class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.shape_car()
        self.velocity = 3

    def get_carcolor(self):
        color = random.choice(COLOR)
        return color

    def shape_car(self):
            self.penup()
            self.shape("square")
            self.hideturtle()
            self.color(self.get_carcolor())
            self.turtlesize(1, 2)
            self.goto(self.get_position())
            self.showturtle()

    def move_car(self, velocity):
        new_x = self.xcor() - velocity
        self.goto(new_x, self.ycor())

    def get_position(self):
        x = BEGGINING_POSITION_X
        y = random.randint(-BEGGINING_POSITION_Y, BEGGINING_POSITION_Y)
        return x, y

    def advance_speed(self, increment):
        self.velocity += increment

