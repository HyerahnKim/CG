from turtle import *
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"


def distance(a, b):
    """ Calculate the Euclidean distance between two points. """
    return math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)


def cross_product(o, a, b):
    """ Return the cross product of vector OA and OB.
        A positive cross product indicates a counter-clockwise turn, 0 indicates a collinear point, and negative indicates a clockwise turn.
    """
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)


def polar_angle(base, p):
    """ Return the polar angle (in radians) from the base point to p adjusted for sorting. """
    return math.atan2(p.y - base.y, p.x - base.x)


def leftmost_point(points):
    """ Find the point with the smallest x-coordinate. If there are ties, select the point with the smallest y-coordinate. """
    return min(points, key=lambda p: (p.x, p.y))


def graham_scan(points):
    """
    Implements Graham's Scan to compute the convex hull.
    Input:
        points: List of Point objects
    Returns:
        convex_hull: List of Point objects forming the convex hull
    """
    # Step 1: Find the leftmost point
    anchor = leftmost_point(points)
    points.remove(anchor)

    # Step 2: Sort the points by polar angle with the anchor, ties broken by distance from the anchor
    points.sort(key=lambda p: (polar_angle(anchor, p), distance(anchor, p)))

    # Step 3: Construct the convex hull using the sorted points
    hull = [anchor]
    for p in points:
        # While there's at least two points in the hull, check for a clockwise turn.
        while len(hull) > 1 and cross_product(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)

    return hull


def visualize(points, convex_hull):
    """
    Visualize the points and the convex hull using turtle graphics.
    Input:
        points: List of Point objects
        convex_hull: List of Point objects forming the convex hull
    """
    # Set up the turtle screen
    screen = Screen()
    screen.title("Convex Hull Visualization")
    screen.setworldcoordinates(-20, -20, 100, 100)

    # Create a turtle object
    pen = Turtle()
    pen.speed(0)  # Fastest speed
    pen.penup()

    # Plot the points
    pen.color("blue")
    for p in points:
        pen.goto(p.x, p.y)
        pen.dot(5)

    # Draw the convex hull
    pen.color("red")
    pen.penup()
    first_point = convex_hull[0]
    pen.goto(first_point.x, first_point.y)
    pen.pendown()
    for p in convex_hull + [first_point]:  # Close the hull
        pen.goto(p.x, p.y)

    # Keep the window open
    screen.mainloop()


# Example Points
points = [
    Point(30, 60), Point(15, 25), Point(0, 30), Point(70, 30),
    Point(50, 40), Point(50, 10), Point(20, 0), Point(55, 20)
]

# Compute Convex Hull
convex_hull = graham_scan(points)

# Visualize the Points and Convex Hull
visualize(points, convex_hull)
