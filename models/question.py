class Question:

    def __init__(self, text: str, answer: str):
        self._text: str = text
        self._answer: str = answer

    @property
    def text(self) -> str:
        return self._text

    @property
    def answer(self) -> str:
        return self._answer
