## Capstone Project

from turtle import Turtle, Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard
import random
import time 

turtle_player = Player()
score = Scoreboard()
screen = Screen()
screen.setup(600, 600)
screen.title("Capstone Turtle")
screen.tracer(0)


screen.listen()
screen.onkey(turtle_player.move, "Up")

cars_conglomerate = []
time_increment = 0.01
level = 1
game_is_on = True
velocity = 3

while game_is_on:

    screen.update()
    time.sleep(time_increment)
    if random.randint(0, 20) >= 20 - 1:
        cars_conglomerate.append(Cars())

    for car in cars_conglomerate:
        car.move_car(velocity)
        # Detect collision
        if car.distance(turtle_player) <= 25:
            # Game over sequence
            score.game_over()
            game_is_on = False

    #Detect a win
    if turtle_player.ycor() >= 250:
        turtle_player.shape_turtle()
        # time_increment -= 0.005
        level += 1
        score.mark_score(level)
        for car in cars_conglomerate:
            car.advance_speed(1)
        velocity += 3

screen.exitonclick()