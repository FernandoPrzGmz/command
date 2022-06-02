from typing import List

from src.commands import AddCommand, SubtractCommand, DivideCommand, MultiplyCommand
from src.interfaces import ICommand


class Calculator:
    def __init__(self):
        self.__result: float = 0.0
        self.__history: List[ICommand] = []

    @property
    def result(self):
        return self.__result

    def __save(self, command):
        if command.is_executed:
            self.__history.append(command)
            self.__result = command.result

    def add(self, num) -> None:
        command = AddCommand(self.__result, num)
        command.execute()
        self.__save(command)

    def subtract(self, num) -> None:
        command = SubtractCommand(self.__result, num)
        command.execute()
        self.__save(command)

    def multiply(self, num) -> None:
        command = MultiplyCommand(self.__result, num)
        command.execute()
        self.__save(command)

    def divide(self, num) -> None:
        command = DivideCommand(self.__result, num)
        command.execute()
        self.__save(command)


