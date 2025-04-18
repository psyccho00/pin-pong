from turtle import Turtle

class Bar(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.goto(pos)
    # right_bar.width=20
    # right_bar.speed("fastest")

    def up(self):
        y=self.ycor()+20
        self.goto(self.xcor(),y)

    def down(self):
        z=self.ycor()-20
        self.goto(self.xcor(),z)
