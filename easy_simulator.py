from arena_sdk import *
# ==== Ниже копировать в симулятор ====
import time
# В данной версии x и y поменяны местами и не работает функция check_point()

# Координаты баз для дронов и ртс
base_drone1 = (-4, -4)
base_drone2 = (-4, -2)

base_rts1 = (-4, 2)
base_rts2 = (-4, 4)

# Координаты всех целей
current_points = [
    (1, -1), (2, 4),
    (-3, -2), (3, 3),
    (2, -2), (-3, 4),
    (1, -4), (4, 4)
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

for point in current_points:
    if point in points_drone1:
        drone1.goto(x=point[0], y=point[1], z=1.5)
        print(f"Дрон 1 летит в точку: {point}")
        time.sleep(10)
        drone1.led_control(255, 0, 0)
        time.sleep(3)
        points_rts1.append(point)
        print(f"Дрон 1 добавил точку: {point} для РТС 1")
        drone1.led_control(0, 0, 0)
    else:
        drone2.goto(x=point[0], y=point[1], z=1.5)
        print(f"Дрон 2 летит в точку: {point}")
        time.sleep(10)
        drone2.led_control(255, 0, 0)
        time.sleep(3)
        points_rts2.append(point)
        print(f"Дрон 2 добавил точку: {point} для РТС 2")
        drone2.led_control(0, 0, 0)
    
drone1.goto(x=base_drone1[0], y=base_drone1[1], z=1.5)
print(f"Дрон 1 летит на базу")
drone2.goto(x=base_drone2[0], y=base_drone2[1], z=1.5)
print(f"Дрон 2 летит на базу")

time.sleep(10)

print(f"Дроны на базе")
print("===============================")

drone1.land()
drone2.land()
time.sleep(5)

drone1.disarm()
drone2.disarm()

print(f"Дроны закончили миссию")
print("===============================")

print(f"Координаты для первого ртс: {points_rts1}")
print(f"Координаты для второго ртс: {points_rts2}")

for point in current_points:
    if point in points_rts1: # Проверка для для кого предназначена точка
        rts1.goto(x=point[0], y=point[1])
        print(f"РТС 1 едет в точку: {point}")
        time.sleep(10)
        rts1.led_control(255, 0, 0)
        time.sleep(3)
        rts1.led_control(0, 0, 0)
        rts1.goto(x=base_rts1[0], y=base_rts1[1])
        print(f"РТС 1 везет ранненого на базу")
        time.sleep(10)
        rts1.led_control(255, 0, 0)
        time.sleep(3)
        rts1.led_control(0, 0, 0)
        print(f"РТС 1 на базе")
    elif point in points_rts2: # Проверка для для кого предназначена точка
        rts2.goto(x=point[0], y=point[1])
        print(f"РТС 2 едет в точку: {point}")
        time.sleep(10)
        rts2.led_control(255, 0, 0)
        time.sleep(3)
        rts2.led_control(0, 0, 0)
        rts2.goto(x=base_rts2[0], y=base_rts2[1])
        print(f"РТС 2 везет ранненого на базу")
        time.sleep(10)
        rts2.led_control(255, 0, 0)
        time.sleep(3)
        rts2.led_control(0, 0, 0)
        print(f"РТС 2 на базе")