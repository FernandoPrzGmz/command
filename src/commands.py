from src.interfaces import ICommand


class AddCommand(ICommand):
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y
        self.__result = None

    @property
    def result(self) -> float:
        return self.__result

    @property
    def is_executed(self) -> bool:
        return self.__result is not None

    def execute(self) -> None:
        self.__result = self.__x + self.__y


class SubtractCommand(ICommand):
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y
        self.__result = None

    @property
    def result(self) -> float:
        return self.__result

    @property
    def is_executed(self) -> bool:
        return self.__result is not None

    def execute(self) -> None:
        self.__result = self.__x - self.__y


class MultiplyCommand(ICommand):
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y
        self.__result = None

    @property
    def result(self) -> float:
        return self.__result

    @property
    def is_executed(self) -> bool:
        return self.__result is not None

    def execute(self) -> None:
        self.__result = self.__x * self.__y


class DivideCommand(ICommand):
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y
        self.__result = None

    @property
    def result(self) -> float:
        return self.__result

    @property
    def is_executed(self) -> bool:
        return self.__result is not None

    def __can_be_executed(self) -> None:
        if self.__y == 0:
            raise ValueError('"y" must be greater than 0.')

    def execute(self) -> None:
        self.__result = self.__x / self.__y


class FactorialCommand(ICommand):
    def __init__(self, x: int):
        self.__x = x
        self.__result = None

    @property
    def result(self) -> float:
        return self.__result

    @property
    def is_executed(self) -> bool:
        return self.__result is not None

    def __can_be_executed(self) -> None:
        if not isinstance(self.__x, int):
            raise ValueError('"x" must be a integral value.')

    def __factorial(self, x) -> int:
        if x in [0, 1]:
            return 1
        else:
            return x * self.__factorial(x-1)

    def execute(self) -> None:
        self.__can_be_executed()
        self.__result = self.__factorial(self.__x)
