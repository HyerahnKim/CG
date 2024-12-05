
'''
Because the leftmost point is same as the lowest point for this example, the result is the same.
'''

from turtle import *
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"


def cross_product(o, a, b):
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)


def jarvis_march(points):
    #Returns: List of Point objects forming the convex hull in counterclockwise order

    # 1. Find the leftmost point
    leftmost = min(points, key=lambda p: p.x)
    hull = []

    current = leftmost
    while True:
        hull.append(current)
        next_point = points[0]
        # 2. For each remaining point, compute the orientation of the triplet
        for p in points:
            if p == current:
                continue
            orientation = cross_product(current, next_point, p)
            if orientation > 0 or (orientation == 0 and distance(current, p) > distance(current, next_point)):
                next_point = p

        current = next_point
        # 3. Repeat until all points are tested
        if current == leftmost:
            break

    return hull


def distance(a, b):
    return (a.x - b.x) ** 2 + (a.y - b.y) ** 2


def visualize(points, hull):
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

    # Draw the convex hull
    pen.color("red")
    pen.penup()
    first_point = hull[0]
    pen.goto(first_point.x, first_point.y)
    pen.pendown()
    for p in hull + [first_point]:  # Close the hull
        pen.goto(p.x, p.y)

    # Keep the window open
    screen.mainloop()


# Input Points
points = [
    Point(2, 0), Point(0, 3), Point(-4, 0), Point(4, 2), Point(5, 1)
]

# Compute Convex Hull using Jarvis March
convex_hull = jarvis_march(points)

# Print Convex Hull Points
print("Convex Hull Points:")
for p in convex_hull:
    print(p)

# Visualize the Convex Hull
visualize(points, convex_hull)
