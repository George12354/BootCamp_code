from turtle import Turtle


# Make a barrier
class Barrier:
    def __init__(self):
        barrier = Turtle("square")
        barrier.color("white")
        barrier.penup()
        x = 0
        y = [290]
        index = 0
        # Try and create a loop for this barrier
        for steps in y:
            barrier.resizemode("user")
            barrier.shapesize(stretch_wid=1, stretch_len=0.2, outline=2)
            barrier.goto(x=x, y=steps)
            barrier.stamp()
            barrier.hideturtle()

            if y[index] == -280:
                break
            else:
                y.append(steps - 30)
                index += 1
