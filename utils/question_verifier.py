from abc import ABC, abstractmethod


class QuestionVerifier(ABC):

    @abstractmethod
    def verify_answer(self) -> bool:
        ...
