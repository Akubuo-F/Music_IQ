from models.question import Question
from utils.ai_api import AIAPI


class QuestionVerifier:

    def __init__(self, ai_api: AIAPI):
        self._ai_api: AIAPI = ai_api

    def verify_question(self, artist_bio: str, question: Question) -> bool:
        ...
