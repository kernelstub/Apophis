from abc import ABC, abstractmethod


class Module(ABC):
    name: str = ""
    description: str = ""
    author: str = ""
    creation_date: str = ""
    module_kind: str = "exploit"

    def __init__(self) -> None:
        pass

    @abstractmethod
    def execute(self) -> None:
        raise NotImplementedError
