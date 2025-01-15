import turtle
import math

# Step 1: Define the polygon vertices
polygon_points = [
    (4, 4), (5, 6), (6, 4), (7, 4), (9, 6), (11, 6),  # Upper points
    (11, -6), (9, -6), (7, -4), (6, -4), (5, -6), (4, -4)  # Lower points
]

# Scale points for better visualization in Turtle
scale = 40
scaled_points = [(x * scale, y * scale) for x, y in polygon_points]

# Step 2: Create a function to draw the polygon
def draw_polygon(points):
    turtle.penup()
    turtle.goto(points[0])
    turtle.pendown()
    for point in points[1:]:
        turtle.goto(point)
    turtle.goto(points[0])  # Close the polygon

# Step 3: Create a function to draw diagonals for triangulation
def draw_diagonal(p1, p2, color="black"):
    turtle.penup()
    turtle.goto(p1)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(p2)

# Step 4: Perform triangulation manually (based on problem setup)
triangles = [
    (scaled_points[0], scaled_points[2], scaled_points[4]),
    (scaled_points[0], scaled_points[4], scaled_points[6]),
    (scaled_points[0], scaled_points[6], scaled_points[8]),
    (scaled_points[0], scaled_points[8], scaled_points[10]),
    (scaled_points[0], scaled_points[10], scaled_points[11]),
]

# Step 5: Draw the triangulation
def draw_triangulation(triangles):
    for triangle in triangles:
        draw_diagonal(triangle[0], triangle[1], color="blue")
        draw_diagonal(triangle[1], triangle[2], color="blue")
        draw_diagonal(triangle[2], triangle[0], color="blue")

# Step 6: Place cameras
# Camera placement based on a simple coloring (e.g., every third vertex)
camera_positions = [scaled_points[1], scaled_points[3], scaled_points[7], scaled_points[9]]

def place_cameras(cameras):
    for camera in cameras:
        turtle.penup()
        turtle.goto(camera)
        turtle.dot(10, "red")  # Mark the camera position

# Step 7: Initialize Turtle
def setup_turtle():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.bgcolor("white")

# Main execution
setup_turtle()
draw_polygon(scaled_points)
draw_triangulation(triangles)
place_cameras(camera_positions)

# Display the result
turtle.done()
