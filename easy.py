from arena_sdk import *
# ==== Ниже копировать в симулятор ====
import time

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
drone2.arm()

drone1.takeoff()
drone2.takeoff()

time.sleep(3)

for point in current_points:
    if point in points_drone1:
        drone1.goto(x=point[0], y=point[1], z=1.5)
        time.sleep(10)
        if drone1.check_point():
            drone1.led_control(255, 0, 0)
            time.sleep(3)
            points_rts1.append(point)
            drone1.led_control(0, 0, 0)
    else:
        drone2.goto(x=point[0], y=point[1], z=1.5)
        time.sleep(10)
        if drone2.check_point():
            drone2.led_control(255, 0, 0)
            time.sleep(3)
            points_rts2.append(point)
            drone2.led_control(0, 0, 0)
    
drone1.goto(x=base_drone1[0], y=base_drone1[1], z=1.5)
drone2.goto(x=base_drone2[0], y=base_drone2[1], z=1.5)
time.sleep(10)

drone1.land()
drone2.land()
time.sleep(5)

drone1.disarm()
drone2.disarm()

for point in current_points:
    if point in points_rts1:
        rts1.goto(x=point[0], y=point[1])
        time.sleep(10)
        rts1.led_control(255, 0, 0)
        time.sleep(3)
        rts1.led_control(0, 0, 0)
        rts1.goto(x=base_rts1[0], y=base_rts1[1])
        time.sleep(10)
        rts1.led_control(255, 0, 0)
        time.sleep(3)
        rts1.led_control(0, 0, 0)
    elif point in points_rts2:
        rts2.goto(x=point[0], y=point[1])
        time.sleep(10)
        rts2.led_control(255, 0, 0)
        time.sleep(3)
        rts2.led_control(0, 0, 0)
        rts2.goto(x=base_rts2[0], y=base_rts2[1])
        time.sleep(10)
        rts2.led_control(255, 0, 0)
        time.sleep(3)
        rts2.led_control(0, 0, 0)