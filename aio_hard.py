from arena_sdk import *
# ==== Ниже копировать в симулятор ====
# Ассинхроный вариант

import asyncio
from operator import itemgetter


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
    (4, -4), (2.4, -3), (4.2, -2), (-1, -3), (-3, -3)
]

# Координаты для двух дронов
points_drone1 = []
points_drone2 = []

# Координаты целей для ртс
points_rts1 = asyncio.Queue()
points_rts2 = asyncio.Queue()

async def drone_mission(drone: Pioneer, points_drone, base, points_rts: asyncio.Queue):
    drone.arm()

    drone.takeoff()
    await asyncio.sleep(3)

    for point in points_drone:
        drone.goto(x=point[0], y=point[1], z=1.5)
        await asyncio.sleep(10)

        if check_point():
            await points_rts.put(point)
            print(f"Добавлена точка {point} для РТС")
            drone.led_control(255, 0, 0)
            await asyncio.sleep(5)
            drone.led_control(0, 0, 0)
    
    await points_rts.put(None)
    drone.goto(base[0], base[1], 1.5)
    await asyncio.sleep(10)
    print("Дрон на базе")
    drone.land()
    await asyncio.sleep(3)
    drone.disarm()

async def rts_mission(rts: Geobot, points_rts: asyncio.Queue, base):
    while True:
        current = await points_rts.get()

        if current is None:
            print("Кончились точки")
            break

        rts.goto(current[0], current[1])
        await asyncio.sleep(10)

        rts.led_control(255, 0, 0)
        await asyncio.sleep(5)
        rts.led_control(0, 0, 0)

        rts.goto(base[0], base[1])
        await asyncio.sleep(10)

        rts.led_control(255, 0, 0)
        await asyncio.sleep(5)
        rts.led_control(0, 0, 0)

        points_rts.task_done()
  
    await asyncio.sleep(1)
        



if __name__ == "__main__":
    drone1 = Pioneer("pioneer1")
    drone2 = Pioneer("pioneer2")

    rts1 = Geobot("geobot1")
    rts2 = Geobot("geobot2")

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

    # Выключение подсветки в симуляторе сначала у всех она горит
    drone1.led_control(0, 0, 0)
    drone2.led_control(0, 0, 0)
    rts1.led_control(0, 0, 0)
    rts2.led_control(0, 0, 0)
    
    task_drone1 = asyncio.create_task(drone_mission(drone1, points_drone1, base_drone1, points_rts1))
    task_drone2 = asyncio.create_task(drone_mission(drone2, points_drone2, base_drone2, points_rts2))

    task_rts1 = asyncio.create_task(rts_mission(rts1, points_rts1, base_rts1))
    task_rts2 = asyncio.create_task(rts_mission(rts2, points_rts2, base_rts2))

    asyncio.gather(task_drone1, task_drone2, task_rts1, task_rts2)
    

