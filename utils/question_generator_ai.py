import json

from openai import OpenAI

from utils.helper import Helper
from utils.question_generator import QuestionGenerator


class QuestionGeneratorAI(QuestionGenerator):

    def __init__(self):
        self._client = OpenAI(api_key=Helper.load_env_variable("OPENAI_CLIENT_SECRET"))

    def generate_questions(self, prompt: str, question_count: int = 3, max_length: int = 50) -> list[dict]:
        engine: str = "gpt-3.5-turbo"
        prompt: str = f"""
        Create {question_count} trivia questions and their answers based on the following 
        text:\n\n{prompt}\n\nFormat the response as a list of dictionaries with 'question' as key
        and 'answer' as value:
        """
        response = self._client.chat.completions.create(
            model=engine,
            messages=[
                {"role": "system", "content": "You are a trivia question generator."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_length * question_count,
            temperature=0.7
        )

        unformatted_str: str = response.choices[0].message.content.replace("`", "")
        questions_as_json_str = QuestionGeneratorAI.clean_openai_response(unformatted_str)
        questions_as_dict: list[dict] = json.loads(questions_as_json_str)
        return questions_as_dict

    @staticmethod
    def clean_openai_response(string: str):
        translation: dict = {
            "`": "",
            "'": "\"",
            "python": "",
            "json": ""
        }
        for target, replacement in translation.items():
            string = string.replace(target, replacement)
        return string.strip()


if __name__ == '__main__':
    question_generator = QuestionGeneratorAI()
    artist_bio = """
    Yuki Chiba, Bio: Yuki Chiba (千葉雄喜, Chiba Yūki, born April 22, 1990), formerly known
    by his stage name KOHH, is a Japanese hip hop rapper and singer from Oji, Kita, Tokyo.
    """
    questions_and_answers = question_generator.generate_questions(artist_bio)
    json_data = {"Yuki Chiba": []}
    for data in questions_and_answers:
        question = data["question"]
        answer = data["answer"]
        print(
            f"Question: {question}, Answer: {answer}"
        )
        json_data["Yuki Chiba"].append(data)
    Helper.save_json_data(json_data, Helper.get_filepath("data/questions_and_answers.json"))
