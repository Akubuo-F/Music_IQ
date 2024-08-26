from models.question import Question


class QuestionService:

    def __init__(self, generator: QuestionGenerator, verifier: QuestionVerifier):
        self._generator: QuestionGenerator = generator
        self._verifier: QuestionVerifier = verifier

    def generate_questions(self, artist_bio: str, questions_count: int = 3) -> list[Question]:
        ...

    def verify_question(self, artist_bio: str, question: Question) -> bool:
        ...
