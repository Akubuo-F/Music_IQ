from abc import ABC, abstractmethod

from utils.savable import Savable


class ModelBuilder:

    @staticmethod
    @abstractmethod
    def build_from_local(local_data: list[str]) -> list[Savable]:
        ...

    @staticmethod
    @abstractmethod
    def build_from_api(api_data: list[dict]) -> list[Savable]:
        ...
