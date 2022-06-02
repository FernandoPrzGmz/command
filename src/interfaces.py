from abc import ABC, abstractmethod


class ICommand(ABC):
    def __init__(self):
        self.is_executed = None

    @abstractmethod
    def execute(self) -> None:
        pass
