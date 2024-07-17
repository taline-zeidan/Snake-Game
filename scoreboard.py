from turtle import Turtle

ALIGN = "center"
FONT = "Courier"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 240)
        self.hideturtle()
        self.speed("fastest")
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGN, font=(FONT, 24, 'normal'))

    def set_new_score(self):
        self.score +=1
        self.clear()
        self.update()

    def game_over(self):
        scoreboard.goto(0, 0)
        scoreboard.write("Game Over.", move=True, align="center", font=("Courier", 24, 'normal'))