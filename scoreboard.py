from turtle import Turtle
STARTING_POSITION = (-100, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.shape_scoreboard()
        self.mark_score(self.level)

    def mark_score(self, level):
        self.clear()
        self.write(f"Level : {level}", False, align="center", font=('Arial', 24, 'normal'))

    def shape_scoreboard(self):
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(STARTING_POSITION)

    def game_over(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=('Arial', 24, 'normal'))