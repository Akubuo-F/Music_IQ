import json
from abc import ABC, abstractmethod


class Savable(ABC):

    @property
    @abstractmethod
    def to_dict(self) -> dict:
        ...

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict) -> "Savable":
        ...

    def save_to_location(self, location: list[str]) -> None:
        location.append(json.dumps(self.to_dict))
