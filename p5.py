import turtle


def setup_turtle():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    return t


def draw_point(t, x, y, name):
    """
    Draws a labeled point (scaled by 100 for visibility).
    """
    t.penup()
    t.goto(x * 100, y * 100)
    t.dot(10, "black")
    t.write(name, align="center", font=("Arial", 12, "normal"))
    t.pendown()


def draw_edges(t, points, edges):
    """
    Draws line segments for each edge in 'edges'.
    """
    for (v1, v2) in edges:
        x1, y1 = points[v1]
        x2, y2 = points[v2]
        t.penup()
        t.goto(x1 * 100, y1 * 100)
        t.pendown()
        t.goto(x2 * 100, y2 * 100)


def main():
    turtle.title("Triangulation of 6 Points (12 edges)")
    t = setup_turtle()

    # Label the points as specified
    points = {
        'A': (0, 4),
        'B': (-2, 0),
        'C': (2, 0),
        'D': (-0.5, 2),
        'E': (0.5, 2),
        'F': (0, 1)
    }

    # These 12 edges ensure a planar triangulation with no crossings.
    edges = [
        # Outer triangle
        ('A', 'B'), ('B', 'C'), ('C', 'A'),
        # Connect interior points to corners
        ('D', 'A'), ('D', 'B'),
        ('E', 'A'), ('E', 'C'),
        ('F', 'C'), ('F', 'B'),
        # Connect interior points among themselves
        ('D', 'E'), ('E', 'F'), ('F', 'D')
    ]

    # Draw the points
    for name, (x, y) in points.items():
        draw_point(t, x, y, name)

    # Draw the edges
    draw_edges(t, points, edges)

    turtle.done()


if __name__ == "__main__":
    main()
