import turtle

# Define the pentagon points
pentagon_points = [(0, 0), (1, 2), (3, 2), (4, 0), (2, -1)]

# Scale points for better visualization
scale = 100
pentagon_points = [(x * scale, y * scale) for x, y in pentagon_points]

# Function to draw the polygon
def draw_polygon(points, label):
    """Draw the polygon."""
    turtle.penup()
    turtle.goto(points[0])
    turtle.pendown()
    for point in points[1:]:
        turtle.goto(point)
    turtle.goto(points[0])  # Close the polygon
    # Write label
    turtle.penup()
    turtle.goto(0, 200)
    turtle.write(label, align="center", font=("Arial", 16, "bold"))

# Function to draw a diagonal
def draw_diagonal(p1, p2, color="blue"):
    """Draw a diagonal."""
    turtle.penup()
    turtle.goto(p1)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(p2)

# Visualize Task 3: Triangulation of the pentagon
def visualize_task3():
    """Visualize the pentagon and its triangulation."""
    turtle.speed(0)
    turtle.hideturtle()
    turtle.setworldcoordinates(-300, -300, 500, 500)

    # Draw the pentagon
    draw_polygon(pentagon_points, "Task 3: Pentagon with 3 Triangles and 7 Edges")

    # Perform triangulation
    diagonals = [
        (pentagon_points[0], pentagon_points[2]),  # Diagonal from (0,0) to (3,2)
        (pentagon_points[0], pentagon_points[3]),  # Diagonal from (0,0) to (4,0)
    ]

    for diagonal in diagonals:
        draw_diagonal(*diagonal)

    # Finish visualization
    turtle.done()

# Run visualization
visualize_task3()
