from abc import ABC, abstractmethod


class QuestionGenerator(ABC):

    @abstractmethod
    def generate_questions(self, prompt: str, question_count: int = 3, max_length: int = 50) -> list[dict]:
        ...
