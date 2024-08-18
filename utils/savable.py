from abc import ABC, abstractmethod
from typing import Any


class Savable(ABC):

    @abstractmethod
    def save(self, location: list[str]) -> None:
        ...

    @classmethod
    @abstractmethod
    def load(cls, object_str: str) -> Any:
        ...

