import turtle

# Define the convex polygon points
polygon_convex = [(5, 0), (3, 2), (-1, 2), (-3, 0), (-1, -2), (3, -2)]

# Scale points for better visualization
scale = 50
polygon_convex = [(x * scale, y * scale) for x, y in polygon_convex]

# Function to draw a polygon
def draw_polygon(points, label, label_position):
    turtle.penup()
    turtle.goto(points[0])
    turtle.pendown()
    for point in points[1:]:
        turtle.goto(point)
    turtle.goto(points[0])  # Close the polygon
    turtle.penup()
    turtle.goto(label_position)
    turtle.write(label, align="center", font=("Arial", 16, "bold"))

# Function to place a camera
def place_camera(position, color):
    turtle.penup()
    turtle.goto(position)
    turtle.dot(20, color)

# Setup Turtle
def setup_turtle():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.bgcolor("white")

# Visualize the convex polygon and single camera
def visualize_case1():
    setup_turtle()
    turtle.setworldcoordinates(-400, -400, 400, 400)

    # Draw the polygon
    draw_polygon(polygon_convex, "Case 1: Convex Polygon, Single Camera", (0, 300))

    # Place a single camera (center of the polygon)
    center = (0, 0)  # Arbitrary point inside the polygon
    place_camera(center, "red")

    # Finish visualization
    turtle.done()

# Run Case 1 visualization
visualize_case1()
