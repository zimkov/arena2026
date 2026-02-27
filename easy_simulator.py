from arena_sdk import *
# ==== Ниже копировать в симулятор ====
import time
from operator import itemgetter
# В данной версии x и y поменяны местами и не работает функция check_point()

def check_point() -> bool:
    return True

# Координаты баз для дронов и ртс
base_drone1 = (-4, -4)
base_drone2 = (-4, -2)

base_rts1 = (-4, 2)
base_rts2 = (-4, 4)

# Координаты всех целей
current_points = [
    (1, 1), (1.3, 2), (3, 3), (-3, 2), (3, 4),
    (4, 4), (2.4, 3), (4.2, 2), (-1, 3), (-3, 3),
    (4, -4), (2.4, -3), (4.2, -2), (-1, -3), (-3, -3),
    (1, -1), (1.3, -2), (3, -3), (-3, -2), (3, 4.2)
]

# Координаты для двух дронов
points_drone1 = []
points_drone2 = []

# Координаты целей для ртс
points_rts1 = []
points_rts2 = []

# Разделение всех координат в зависимости от X 
for point in current_points:
    if point[1] < 0:
        points_drone1.append(point)
    else:
        points_drone2.append(point)

# Сортировка по удалению от базы для оптимизации маршрута
points_drone1.sort(key=itemgetter(0))
points_drone2.sort(key=itemgetter(0))

print(f"Координаты для первого дрона: {points_drone1}")
print(f"Координаты для второго дрона: {points_drone2}")


# Создание объекта дрона и ртс в онлайн-симуляторе
drone1 = Pioneer("pioneer1")
drone2 = Pioneer("pioneer2")

rts2 = Geobot("geobot1")
rts1 = Geobot("geobot2")

# Выключение подсветки в симуляторе сначала у всех она горит
drone1.led_control(0, 0, 0)
drone2.led_control(0, 0, 0)
rts1.led_control(0, 0, 0)
rts2.led_control(0, 0, 0)

drone1.arm()
print(f"Дрон 1 завел моторы")
drone2.arm()
print(f"Дрон 2 завел моторы")

drone1.takeoff()
print(f"Дрон 1 взлетает")
drone2.takeoff()
print(f"Дрон 2 взлетает")

time.sleep(3)

print(f"Дроны взлетели")
print("===============================")


drone1_have_points = False
drone2_have_points = False

rts1_have_points = False
rts2_have_points = False

for i in range(20):
    # Проверки на наличие точек для дронов
    if i < len(points_drone1) and i < len(points_drone2):
        drone1_have_points = True
        drone2_have_points = True
    elif i == len(points_drone1) and i < len(points_drone2):
        drone1_have_points = False
        drone2_have_points = True
        print(f"Дрон 1 закончил миссию")
    elif i < len(points_drone1) and i == len(points_drone2):
        drone1_have_points = True
        drone2_have_points = False
        print(f"Дрон 2 закончил миссию")
    elif i == len(points_drone1) or i == len(points_drone2):
        drone1_have_points = False
        drone2_have_points = False
        print(f"Дроны закончили миссию")
        
    if drone1_have_points or drone2_have_points:
        
        if drone1_have_points:
            point1 = (points_drone1[i][0], points_drone1[i][1])
            drone1.goto(x=point1[0], y=point1[1], z=1.5)
            print(f"Дрон 1 летит в точку: {point1}")

        if drone2_have_points:
            point2 = (points_drone2[i][0], points_drone2[i][1])
            drone2.goto(x=point2[0], y=point2[1], z=1.5)
            print(f"Дрон 2 летит в точку: {point2}")

        time.sleep(10)

        if drone1_have_points: drone1.led_control(255, 0, 0)
        if drone2_have_points: drone2.led_control(255, 0, 0)

        time.sleep(5)

        if check_point() and drone1_have_points:
            points_rts1.append(point1)
            print(f"Дрон 1 добавил точку: {point1} для РТС 1")

        if check_point() and drone2_have_points:
            points_rts2.append(point2)
            print(f"Дрон 2 добавил точку: {point2} для РТС 2")

        if drone1_have_points: drone1.led_control(0, 0, 0)
        if drone2_have_points: drone2.led_control(0, 0, 0)


drone1.goto(x=base_drone1[0], y=base_drone1[1], z=1.5)
print(f"Дрон 1 летит на базу")
drone2.goto(x=base_drone2[0], y=base_drone2[1], z=1.5)
print(f"Дрон 2 летит на базу")
time.sleep(10)

drone1.land()
drone2.land()
time.sleep(5)

drone1.disarm()
drone2.disarm()
print(f"Дроны на базе")
print("===============================")
#=========================
    
print(f"Дроны закончили миссию")
print("===============================")

print(f"Координаты для первого ртс: {points_rts1}")
print(f"Координаты для второго ртс: {points_rts2}")

count_points = 0 # Максимальное кол-во точек для одной РТС
if len(points_rts1) > len(points_rts2):
    count_points = len(points_rts1)
else:
    count_points = len(points_rts2)

print(f"Максимальное кол-во точек для одной РТС: {count_points}")

for i in range(count_points):
    # Проверка если есть точки для обоих ртс
    if i < len(points_rts1) and i < len(points_rts2):

        point1 = (points_rts1[i][0], points_rts1[i][1])
        point2 = (points_rts2[i][0], points_rts2[i][1])

        rts1.goto(x=point1[0], y=point1[1])
        rts2.goto(x=point2[0], y=point2[1])

        print(f"РТС 1 едет в точку: {point1}")
        print(f"РТС 2 едет в точку: {point2}")

        time.sleep(10)

        rts1.led_control(255, 0, 0)
        rts2.led_control(255, 0, 0)

        time.sleep(5)

        rts1.led_control(0, 0, 0)
        rts2.led_control(0, 0, 0)

        rts1.goto(base_rts1[0], base_rts1[1])
        rts2.goto(base_rts2[0], base_rts2[1])

        print(f"РТС 1 везет ранненого на базу")
        print(f"РТС 2 везет ранненого на базу")

        time.sleep(10)

        rts1.led_control(255, 0, 0)
        rts2.led_control(255, 0, 0)

        time.sleep(5)

        rts1.led_control(0, 0, 0)
        rts2.led_control(0, 0, 0)

    elif i < len(points_rts1): # Проверка если состались точки для первого ртс
        point1 = (points_rts1[i][0], points_rts1[i][1])

        rts1.goto(x=point1[0], y=point1[1])
        print(f"РТС 1 едет в точку: {point1}")
        time.sleep(10)

        rts1.led_control(255, 0, 0)
        time.sleep(5)
        rts1.led_control(0, 0, 0)

        rts1.goto(base_rts1[0], base_rts1[1])
        print(f"РТС 1 везет ранненого на базу")
        time.sleep(10)

        rts1.led_control(255, 0, 0)
        time.sleep(5)
        rts1.led_control(0, 0, 0)
    
    elif i < len(points_rts2): # Проверка если состались точки для второго ртс
        point2 = (points_rts2[i][0], points_rts2[i][1])

        rts2.goto(x=point2[0], y=point2[1])
        print(f"РТС 2 едет в точку: {point2}")
        time.sleep(10)

        rts2.led_control(255, 0, 0)
        time.sleep(5)
        rts2.led_control(0, 0, 0)

        rts2.goto(base_rts2[0], base_rts2[1])
        print(f"РТС 2 везет ранненого на базу")
        time.sleep(10)

        rts2.led_control(255, 0, 0)
        time.sleep(5)
        rts2.led_control(0, 0, 0)