import turtle

# Define the non-convex polygon points
polygon_nonconvex = [(5, 0), (3, 2), (-1, 2), (-3, 0), (-1, -4), (3, -2)]

# Scale points for better visualization
scale = 50
polygon_nonconvex = [(x * scale, y * scale) for x, y in polygon_nonconvex]

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

# Function to place cameras
def place_camera(position, color):
    turtle.penup()
    turtle.goto(position)
    turtle.dot(20, color)

# Setup Turtle
def setup_turtle():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.bgcolor("white")

# Visualize the non-convex polygon and two cameras
def visualize_case2():
    setup_turtle()
    turtle.setworldcoordinates(-400, -400, 400, 400)

    # Draw the polygon
    draw_polygon(polygon_nonconvex, "Case 2: Non-Convex Polygon, Two Cameras", (0, 300))

    # Place two cameras strategically
    camera_1 = polygon_nonconvex[1]  # Near the top vertex
    camera_2 = polygon_nonconvex[4]  # Near the reflex vertex
    place_camera(camera_1, "blue")
    place_camera(camera_2, "green")

    # Finish visualization
    turtle.done()

# Run Case 2 visualization
visualize_case2()
