from models.question import Question
from utils.ai_api_client import AIAPIClient


class QuestionService:

    def __init__(self, ai_api: AIAPIClient):
        self._ai_api: AIAPIClient = ai_api

    def generate_questions(self, artist_bio: str, questions_count: int = 3) -> list[Question]:
        ...

    def verify_question(self, artist_bio: str, question: Question) -> bool:
        ...
