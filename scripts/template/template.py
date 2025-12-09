from dataclasses import dataclass
from core.modular import Module

@dataclass
class ExploitMeta:
    name: str
    description: str
    author: str
    creation_date: str


class Exploit(Module):
    def __init__(self) -> None:
        meta = ExploitMeta(
            name="test",
            description="Example description of this exploit.",
            author="username",
            creation_date="10-10-2025",
        )
        self.meta: ExploitMeta = meta
        self.name: str = meta.name
        self.description: str = meta.description
        self.author: str = meta.author
        self.creation_date: str = meta.creation_date

    def execute(self) -> None:
        print("Hello world!")
        ChildClass.execute()


class ChildClass:
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def execute() -> None:
        print("Hello child class!")

    