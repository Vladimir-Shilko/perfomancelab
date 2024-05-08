import sys

def read_circle_data(file_path):
    with open(file_path, 'r') as file:
        x, y = map(float, file.readline().split())
        radius = float(file.readline())
        return (x, y, radius)

def read_points(file_path):
    with open(file_path, 'r') as file:
        points = []
        for line in file:
            x, y = map(float, line.split())
            points.append((x, y))
        return points

def calculate_point_position(circle_center, radius, point):
    distance_squared = (point[0] - circle_center[0])**2 + (point[1] - circle_center[1])**2
    if distance_squared == radius**2:
        return 0  # Точка лежит на окружности
    elif distance_squared < radius**2:
        return 1  # Точка внутри окружности
    else:
        return 2  # Точка снаружи окружности

if __name__ == "__main__":

    circle_file_path = sys.argv[1]
    points_file_path = sys.argv[2]
    # circle_file_path = 'circle.txt'
    # points_file_path = 'dot.txt'
    circle_data = read_circle_data(circle_file_path)
    points = read_points(points_file_path)

    circle_center = (circle_data[0], circle_data[1])
    radius = circle_data[2]

    for point in points:
        position = calculate_point_position(circle_center, radius, point)
        print(position)