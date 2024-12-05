from turtle import *
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"


def cross_product(o, a, b):
    """
    Compute the cross product of vectors OA and OB.
    Positive value: Counterclockwise turn
    Negative value: Clockwise turn
    Zero value: Collinear points
    """
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)


def distance(a, b):
    """ Compute the squared distance between two points. """
    return (a.x - b.x) ** 2 + (a.y - b.y) ** 2


def find_successor(points, current, pen):
    """
    Find the successor of the current point on the convex hull.
    Input:
        points: List of Point objects
        current: Current point being processed
        pen: Turtle object for visualization
    Returns:
        next_point: The next point on the convex hull
    """
    next_point = points[0]
    for p in points:
        if p == current:
            continue
        # Visualize the test
        pen.penup()
        pen.color("gray")
        pen.goto(current.x, current.y)
        pen.pendown()
        pen.goto(p.x, p.y)
        orientation = cross_product(current, next_point, p)
        if orientation > 0 or (orientation == 0 and distance(current, p) > distance(current, next_point)):
            next_point = p

    return next_point


def jarvis_march(points, pen):
    """
    Implement the Jarvis March (Gift Wrapping) algorithm to find the convex hull.
    Input:
        points: List of Point objects
        pen: Turtle object for visualization
    Returns:
        hull: List of Point objects forming the convex hull in counterclockwise order
    """
    # Find the lowest point
    lowest = min(points, key=lambda p: (p.y, p.x))
    hull = []

    # Start wrapping
    current = lowest
    while True:
        hull.append(current)
        next_point = find_successor(points, current, pen)

        # Visualize the hull edge
        pen.color("red")
        pen.penup()
        pen.goto(current.x, current.y)
        pen.pendown()
        pen.goto(next_point.x, next_point.y)

        current = next_point
        if current == lowest:
            break

    return hull


def visualize(points, hull):
    """
    Visualize the points and the convex hull using turtle graphics.
    Input:
        points: List of Point objects
        hull: List of Point objects forming the convex hull
    """
    # Set up the turtle screen
    screen = Screen()
    screen.title("Jarvis March Visualization")
    screen.setworldcoordinates(-10, -10, 10, 10)

    # Create a turtle object
    pen = Turtle()
    pen.speed(0)  # Fastest speed
    pen.penup()

    # Plot all points
    pen.color("blue")
    for p in points:
        pen.goto(p.x, p.y)
        pen.dot(5, "blue")
        pen.write(f"{p}", align="center", font=("Arial", 8, "normal"))

    # Compute Convex Hull
    hull = jarvis_march(points, pen)

    # Keep the window open
    screen.mainloop()


# Input Points
points = [
    Point(2, 0), Point(0, 3), Point(-4, 0), Point(4, 2), Point(5, 1)
]

# Visualize the Convex Hull
visualize(points, None)
