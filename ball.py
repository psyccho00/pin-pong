from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move= 10
        self.y_move= 10
        self.move_speed = 0.1


    def move(self):
        x=self.xcor() + self.x_move
        y=self.ycor() + self.y_move
        self.goto(x,y)

    def bounce(self):
        self.y_move *= -1

    def collide(self):
        self.x_move*= -1
        self.move_speed *=0.9

    def come_middle(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.collide()

