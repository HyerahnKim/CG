import turtle


def setup_turtle():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    return t


def draw_triangle(t, points, color):
    t.fillcolor(color)
    t.begin_fill()
    t.goto(points[0][0] * 50, points[0][1] * 50)
    t.goto(points[1][0] * 50, points[1][1] * 50)
    t.goto(points[2][0] * 50, points[2][1] * 50)
    t.goto(points[0][0] * 50, points[0][1] * 50)
    t.end_fill()


def main():
    turtle.title("3-Colorable Face Coloring of Triangulation with 3 Colors")
    t = setup_turtle()
    points = {
        'A': (-4, 4), 'B': (-4, -4), 'C': (4, -4),
        'D': (4, 4), 'E': (0, 2), 'F': (-2, -2), 'G': (2, -2)
    }

    # Define triangles and assign colors from a palette of three
    triangles = [
        (('A', 'B', 'F'), 'red'),
        (('B', 'F', 'G'), 'green'),
        (('B', 'C', 'G'), 'red'),
        (('F', 'G', 'E'), 'blue'),
        (('A', 'F', 'E'), 'green'),
        (('A', 'D', 'E'), 'red'),
        (('D', 'E', 'G'), 'green'),
        (('D', 'C', 'G'), 'blue')
    ]

    # Draw triangles
    for triangle in triangles:
        coords = [points[triangle[0][0]], points[triangle[0][1]], points[triangle[0][2]]]
        draw_triangle(t, coords, triangle[1])

    # Draw points on top of triangles to visualize vertices
    for name, coord in points.items():
        t.penup()
        t.goto(coord[0] * 50, coord[1] * 50)  # scaled for visibility
        t.dot(10, "black")
        t.write(name, align="center", font=("Arial", 12, "normal"))

    turtle.done()


if __name__ == "__main__":
    main()
