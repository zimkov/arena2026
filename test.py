
def drone_mission():
    pass

if __name__ == "__main__":

    points = [
        (-3, 5),
        (0, 0),
        (-1, 0),
        (0, 0),
        (1, 1),
        (-3, 5),
        (3, -1),
        (-1, -1),
        (0, 0),
        (-2, 1)
    ]

    points1 = []
    points2 = []

    for point in points:
        if point[0] < 0:
            points1.append(point)
        else:
            points2.append(point)
    
    print(f"Массив точек для первого дрона: {points1}")
    print(f"Массив точек для второго дрона: {points2}")