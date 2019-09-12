#################################################################################
# Author: Zy'Shavia Garrett & Shawn Villahermosa
# Username: garrettz, villahermosas
#
# Assignment: T03: Boustrophedon Turtles
# Purpose: To very simply demonstrate the turtle library to demo shapes and using images for shapes
#################################################################################
# Acknowledgements:
#
# Dr. Heggen helped us with making the program work using functions
#
#################################################################################

import turtle


def different_color_square(shavia, size):
    """
    :param size: Not being used
    :param shavia: a Turtle object
    :return: None
    """
    # Puts different colors on edges
    shavia.begin_fill()
    for color in ["red", "yellow", "blue", "green"]:  # Color can either be red, blue, green, or purple
        shavia.color(color)
        shavia.forward(50)
        shavia.right(90)
        shavia.color("white")  # Fills each square white
    shavia.end_fill()


def main():
    wn = turtle.Screen()
    wn.title("Squares!")
    wn.bgcolor("black")  # Makes the background color black

    shavia = turtle.Turtle()
    shavia.pensize(5)
    shavia.hideturtle()

    size = 10
    for square in range(4):
        different_color_square(shavia, size)
        size = size + 10  # Increase the size for next iteration
        shavia.left(90)
        shavia.forward(20)

    wn.exitonclick()


main()
