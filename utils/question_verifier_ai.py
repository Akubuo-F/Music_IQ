from utils.question_verifier import QuestionVerifier

from fuzzywuzzy import fuzz


class QuestionVerifierAI(QuestionVerifier):

    def __init__(self, correct_answer: str, user_answer: str):
        self._correct_answer: str = QuestionVerifierAI.normalize_answer(correct_answer)
        self._user_answer: str = QuestionVerifierAI.normalize_answer(user_answer)

    def verify_answer(self) -> bool:
        if (len(self.correct_answer.split()) == 1 and len(self.user_answer.split()) == 1) and \
                self.correct_answer != self.user_answer:
            return False
        return fuzz.partial_ratio(self.correct_answer, self.user_answer) > 80

    @staticmethod
    def normalize_answer(answer: str) -> str:
        words: list[str] = (
            answer.lower()
            .strip()
            .split()
        )
        normalized_answer: str = " ".join(sorted(words))
        return normalized_answer

    @property
    def correct_answer(self) -> str:
        return self._correct_answer

    @property
    def user_answer(self) -> str:
        return self._user_answer


if __name__ == '__main__':
    def test1():
        expected = "April 22, 1990"
        answer = "april 1990"
        question_verifier = QuestionVerifierAI(expected, answer)
        if question_verifier.verify_answer():
            return "correct"
        else:
            return "wrong"

    def test2():
        expected = "Oji, Kita, Tokyo"
        answer = "tokyo oji kita"
        question_verifier = QuestionVerifierAI(expected, answer)
        if question_verifier.verify_answer():
            return "correct"
        else:
            return "wrong"

    def test3():
        expected = "yuki chiba"
        answer = "chib yuki"
        question_verifier = QuestionVerifierAI(expected, answer)
        if question_verifier.verify_answer():
            return "correct"
        else:
            return "wrong"

    def test4():
        expected = "KHOO"
        answer = "kh"
        question_verifier = QuestionVerifierAI(expected, answer)
        if question_verifier.verify_answer():
            return "correct"
        else:
            return "wrong"

    def test5():
        expected = "Megan Thee Stallion"
        answer = "magan the stallion"
        question_verifier = QuestionVerifierAI(expected, answer)
        if question_verifier.verify_answer():
            return "correct"
        else:
            return "wrong"

    def test6():
        expected = "Megan Thee Stallion"
        answer = "maga the sta"
        question_verifier = QuestionVerifierAI(expected, answer)
        if question_verifier.verify_answer():
            return "correct"
        else:
            return "wrong"

    def test7():
        expected = "Megan Thee Stallion"
        answer = "megan"
        question_verifier = QuestionVerifierAI(expected, answer)
        if question_verifier.verify_answer():
            return "correct"
        else:
            return "wrong"


    tests = (
        test1,
        test2,
        test3,
        test4,
        test5,
        test6,
        test7
    )
    for idx, test in enumerate(tests, start=1):
        print(f"Test {idx} = {test()}")
