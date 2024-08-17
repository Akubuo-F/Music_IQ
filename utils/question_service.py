from models.question import Question
from utils.ai_api_client import AIAPI


class QuestionService:

    def __init__(self, ai_api: AIAPI):
        self._ai_api: AIAPI = ai_api

    def generate_questions(self, artist_bio: str, question_count: int = 3) -> list[Question]:
        ...

    def verify_question(self, artist_bio: str, question: Question) -> bool:
        ...
