import sys

def point_ellipse_position(x0, y0, a, b, x, y):
    ellipse = ((x - x0) ** 2) / (a ** 2) + ((y - y0) ** 2) / (b ** 2)
    if ellipse < 1:
        return 1  # внутри
    elif ellipse > 1:
        return 2  # снаружи
    else:
        return 0  # на эллипсе

ellipse_file = sys.argv[1]
points_file = sys.argv[2]

with open(ellipse_file, 'r') as ellipse_f:
    x0, y0 = map(float, ellipse_f.readline().split())
    a, b = map(float, ellipse_f.readline().split())

points = []
with open(points_file, 'r') as points_f:
    for line in points_f:
        x, y = map(float, line.split())
        points.append((x, y))

if not (1 <= len(points) <= 100):
    print("Количество точек должно быть от 1 до 100.")
    sys.exit(1)

for x, y in points:
    print(point_ellipse_position(x0, y0, a, b, x, y))
