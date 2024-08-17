from abc import ABC, abstractmethod


class AIAPIClient(ABC):

    @abstractmethod
    def get_response(self, prompt: str) -> dict[str, str]:
        ...
