from arena_sdk import *
# ==== Ниже копировать в симулятор ====
import time

def go_while(robot, dest_x: float, dest_y: float) -> bool:
    """
        Следовать в точку пока не достигнет
        :param robot: дрон либо машинка
        :param dest_x: целевая x координата
        :param dest_y: целевая y координата
    """
    err = 0.3 # Погрешность
    while True:
        real_x = robot.position[0]
        real_y = robot.position[1]
        if (dest_x - err <= real_x + err) and (dest_y - err <= dest_y + err):
            break
        else:
            if type(robot) is Pioneer:
                robot.goto(x=dest_x, y=dest_y, z=1.5)
            elif type(robot) is Geobot:
                robot.goto(x=dest_x, y=dest_y)
            time.sleep(3)
    return True

# Координаты баз для дронов и ртс
base_drone1 = ()
base_drone2 = ()

base_rts1 = ()
base_rts2 = ()

# Координаты всех целей
current_points = [
    (), (), (), (), (),
    (), (), (), (), (),
    (), (), (), (), (),
    (), (), (), (), ()
]

# Координаты для двух дронов
points_drone1 = []
points_drone2 = []

# Координаты целей для ртс
points_rts1 = []
points_rts2 = []

# Разделение всех координат в зависимости от X
for point in current_points:
    if point[0] < 0:
        points_drone1.append(point)
    else:
        points_drone2.append(point)

print(f"Координаты для первого дрона: {points_drone1}")
print(f"Координаты для второго дрона: {points_drone2}")


# Создание объекта дрона и ртс в онлайн-симуляторе
drone1 = Pioneer("pioneer1")
drone2 = Pioneer("pioneer2")

rts1 = Geobot("geobot1")
rts2 = Geobot("geobot2")

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
        go_while(drone1, point[0], point[1])
        print(f"Дрон 1 летит в точку: {point}")

        if drone1.check_point():
            drone1.led_control(255, 0, 0)
            time.sleep(3)
            points_rts1.append(point)
            print(f"Дрон 1 добавил точку: {point} для РТС 1")
            drone1.led_control(0, 0, 0)
    else:
        go_while(drone2, point[0], point[1])
        print(f"Дрон 2 летит в точку: {point}")

        if drone2.check_point():
            drone2.led_control(255, 0, 0)
            time.sleep(3)
            points_rts2.append(point)
            print(f"Дрон 2 добавил точку: {point} для РТС 2")
            drone2.led_control(0, 0, 0)

print(f"Дрон 1 летит на базу")   
go_while(robot=drone1, dest_x=base_drone1[0], dest_y=base_drone1[1])
print(f"Дрон 2 летит на базу")
go_while(robot=drone2, dest_x=base_drone2[0], dest_y=base_drone2[1])


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
        go_while(robot=rts1, dest_x=point[0], dest_y=point[1])
        print(f"РТС 1 едет в точку: {point}")

        rts1.led_control(255, 0, 0)
        time.sleep(3)
        rts1.led_control(0, 0, 0)
        go_while(robot=rts1, dest_x=base_rts1[0], dest_y=base_rts1[1])
        print(f"РТС 1 везет ранненого на базу")

        rts1.led_control(255, 0, 0)
        time.sleep(3)
        rts1.led_control(0, 0, 0)
        print(f"РТС 1 на базе")
    elif point in points_rts2: # Проверка для для кого предназначена точка
        go_while(robot=rts2, dest_x=point[0], dest_y=point[1])
        print(f"РТС 2 едет в точку: {point}")

        rts2.led_control(255, 0, 0)
        time.sleep(3)
        rts2.led_control(0, 0, 0)
        go_while(robot=rts2, dest_x=base_rts2[0], dest_y=base_rts2[1])
        print(f"РТС 2 везет ранненого на базу")

        rts2.led_control(255, 0, 0)
        time.sleep(3)
        rts2.led_control(0, 0, 0)
        print(f"РТС 2 на базе")