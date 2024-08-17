from models.question import Question
from utils.ai_api import AIAPI


class QuestionGenerator:

    def __init__(self, ai_api: AIAPI):
        self._ai_api: AIAPI

    def generate_question(self, artist_bio: str) -> Question:
        ...
