from typing import List

class Pioneer:
    def __init__(self, name: str) -> None:
        """Инициализация дрона по имени"""
        pass

    def arm(self) -> None:
        """Включение двигателей"""
        pass

    def disarm(self) -> None:
        """Выключение двигателей"""
        pass

    def takeoff(self, altitude: float = 1.5) -> None:
        """
        Взлет
        :param altitude: высота на которую надо подняться
        """
        pass

    def land(self) -> None:
        """Посадка (с дизармом после посадки)"""
        pass

    def goto(self, x: float, y: float, z: float) -> None:
        """
        Следовать в точку
        :param x: x координата
        :param y: y координата
        :param z: z координата
        """
        pass

    def led_control(self, r: int, g: int, b: int) -> None:
        """
        Установить световую индикацию в заданный цвет
        :param r: насыщенность красного 0-255
        :param g: насыщенность зеленого 0-255
        :param b: насыщенность синего 0-255
        """
        pass

    def check_point(self) -> bool:
        """Проверка точки в которой находится дрон"""
        return True

    @property
    def position(self) -> List[float]:
        """
        Получение списка координат, в которых находится дрон
        ВАЖНО: это свойство, вызывать без скобок!
        """
        return [0.0, 0.0, 0.0]


class Geobot:
    def __init__(self, name: str) -> None:
        """Инициализация РТС по имени"""
        pass

    def goto(self, x: float, y: float) -> None:
        """
        Следовать в точку
        :param x: x координата
        :param y: y координата
        """
        pass

    def led_control(self, r: int, g: int, b: int) -> None:
        """
        Установить световую индикацию в заданный цвет
        :param r: насыщенность красного 0-255
        :param g: насыщенность зеленого 0-255
        :param b: насыщенность синего 0-255
        """
        pass

    @property
    def position(self) -> List[float]:
        """
        Получение списка координат, в которых находится РТС
        ВАЖНО: это свойство, вызывать без скобок!
        """
        return [0.0, 0.0]