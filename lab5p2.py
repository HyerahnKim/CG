class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"({self.x}, {self.y})"

def is_inside_square(m):
    return -3 <= m.x <= 3 and -3 <= m.y <= 3

# Define Points
A = Point(3, -3)
B = Point(3, 3)
C = Point(-3, -3)
D = Point(-3, 3)

# Test for different values of lambda
for lam in [-3, -2, -1, 0, 1, 2, 3]:
    M = Point(2 - lam, 3 + lam)
    if is_inside_square(M):
        convex_hull_points = [A, B, C, D]
    else:
        convex_hull_points = [A, B, C, D, M]
    print(f"Lambda = {lam}: Convex Hull Points = {len(convex_hull_points)}")


print("\n--- Result Summary ---")
print("- When -1 ≤ λ ≤ 0: The convex hull is a square and the number of points is 4")
print("- When λ < -1 or λ > 0: Number of points on the convex hull is 5 including λ")
