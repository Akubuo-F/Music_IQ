from models.question import Question
from utils.ai_api import AIAPI


class QuestionGenerator:

    def __init__(self, ai_api: AIAPI):
        self._ai_api: AIAPI = ai_api

    def generate_questions(self, artist_bio: str, question_count: int = 3) -> list[Question]:
        ...
