'''
centroid-based polar sorting algorithm and its time complexity analysis:

1. Centroid calculation:
Computing the centroid involves summing the x- and y-coordinates of all n points, which takes O(n).

2. Polar angle sorting:
Sorting the n points by their polar angle relative to the centroid is the dominant step, with a complexity of O(n log n).

3. Total complexity:
The centroid calculation is O(n), and sorting is O(n log n).
Therefore, the total complexity is O(n log n).
'''

import math
from turtle import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"


def compute_centroid(points):
    """ Compute the centroid of the given points. """
    n = len(points)
    x_sum = sum(p.x for p in points)
    y_sum = sum(p.y for p in points)
    return Point(x_sum / n, y_sum / n)


def sort_points_by_polar_angle(points, centroid):
    """ Sort points by polar angle relative to the centroid. """

    def polar_angle(p):
        return math.atan2(p.y - centroid.y, p.x - centroid.x)

    return sorted(points, key=polar_angle)


def arrange_polygon(points):
    """ Arrange points into a valid polygon. """
    # Step 1: Compute the centroid
    centroid = compute_centroid(points)

    # Step 2: Sort points by polar angle relative to the centroid
    sorted_points = sort_points_by_polar_angle(points, centroid)

    return sorted_points, centroid


def visualize_polygon(points, polygon, centroid):
    """ Visualize the points and the constructed polygon using turtle. """
    # Set up the turtle screen
    screen = Screen()
    screen.title("Polygon Visualization")
    screen.setworldcoordinates(-10, -10, 10, 10)

    # Create a turtle object
    pen = Turtle()
    pen.speed(0)  # Fastest speed
    pen.penup()

    # Plot the centroid
    pen.color("green")
    pen.goto(centroid.x, centroid.y)
    pen.dot(8, "green")
    pen.write("Centroid", align="center", font=("Arial", 10, "normal"))

    # Plot all points
    pen.color("blue")
    for p in points:
        pen.goto(p.x, p.y)
        pen.dot(5, "blue")
        pen.write(f"{p}", align="center", font=("Arial", 8, "normal"))

    # Draw the polygon
    pen.color("red")
    pen.penup()
    first_point = polygon[0]
    pen.goto(first_point.x, first_point.y)
    pen.pendown()
    for p in polygon + [first_point]:  # Close the polygon
        pen.goto(p.x, p.y)

    # Keep the window open
    screen.mainloop()


# Input Points
points = [
    Point(4, 2), Point(7, 1), Point(-3, 5), Point(3, 6),
    Point(-4, -4), Point(-1, 1), Point(2, -6)
]

# Arrange points into a polygon
polygon, centroid = arrange_polygon(points)

# Visualize the results
visualize_polygon(points, polygon, centroid)
