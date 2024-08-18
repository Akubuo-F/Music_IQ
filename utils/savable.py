from abc import ABC, abstractmethod


class Savable(ABC):

    @abstractmethod
    def save(self, location: list[str]) -> None:
        ...

    @classmethod
    @abstractmethod
    def load(cls, object_str: str) -> "Savable":
        ...

    @classmethod
    def from_object_str(cls, data: str) -> "Savable":
        ...

    @classmethod
    def from_dict(cls, data: dict) -> "Savable":
        ...
