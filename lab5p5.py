class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def cross_product(o, a, b):
    # Cross product of vector OA and OB
    # A positive cross product indicates a counter-clockwise turn, 0 indicates collinear points, and negative indicates a clockwise turn
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

def andrews_scan(points):
    # Sort the points lexicographically (tuples are compared lexicographically)
    # Remove duplicates to detect the case we have just one unique point
    points = sorted(set(points), key=lambda p: (p.x, p.y))

    # Boring case: no points or a single point, possibly repeated multiple times.
    if len(points) <= 1:
        return points

    # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
    # Returns a positive value, if OAB makes a counter-clockwise turn,
    # negative for clockwise turn, and zero if the points are collinear.
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    return lower

# Define points based on the problem statement
points = [Point(1, 11), Point(2, 7), Point(3, 8), Point(4, 10), Point(5, 7), Point(6, 7), Point(7, 11)]

# Calculate lower convex hull
lower_hull = andrews_scan(points)

# Output the points in the lower hull
print("Lower hull points:")
for point in lower_hull:
    print(f"({point.x}, {point.y})")
