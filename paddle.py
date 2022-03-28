from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, position_x, position_y):
        """pass the paddles position """

        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position_x, position_y)

    def move_up(self):
        new_y = self.ycor() + 30
        self.goto(x=self.xcor(), y=new_y)

    def move_down(self):

        new_y = self.ycor() - 30
        self.goto(x=self.xcor(), y=new_y)







