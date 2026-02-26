import threading
import time
import queue


array_coord = queue.Queue()

def drone(name):
    global array_coord
    print(f"{name} начал работу")
    time.sleep(2)
    for i in range(5):
        array_coord.put((i, name))
        print(f"{name} записал координаты")
        time.sleep(3)
    print(f"{name} закончил работу")

def rts(name):
    global array_coord
    print(f"{name} начал работу")
    while True:
        try:
            current = array_coord.get(timeout=5)
            print(f"{name} поехал на координаты {current}")
            time.sleep(5)
            print(f"{name} забрал цель {current}")
            array_coord.task_done()
        except queue.Empty:
            print('Координат больше нет')
            break
    time.sleep(1)
    print(f"{name} закончил работу") 

def check_point() -> bool:
    return True

if __name__ == "__main__":

    points = [
        (-3, 5),
        (0, 0),
        (0, 0),
        (0, 0),
        (1, 1),
        (-3, 5),
        (0, 0),
        (0, 0),
        (0, 0),
        (1, 1)
    ]

    points1 = []
    points2 = []

    for point in points:
        if point[0] < 0:
            points1.append(point)
        else:
            points2.append(point)
    
    print(points1)
    print(points2)

    thread1 = threading.Thread(target=drone, args=("Дрон 1",))
    thread2 = threading.Thread(target=rts, args=("РТС 1",))
    thread3 = threading.Thread(target=drone, args=("Дрон 2",))
    thread4 = threading.Thread(target=rts, args=("РТС 2",))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    print("Программа завершена")
