import json
import os
from dotenv import load_dotenv


class Helper:

    @staticmethod
    def load_env_variable(key: str) -> str:
        load_dotenv()
        return os.getenv(key)

    @staticmethod
    def get_filepath(filename: str) -> str:
        current_dir: str = os.path.abspath(__file__)
        root_dir: str = os.path.dirname(current_dir)
        navigation_count: int = 1
        back_navigation: str = "../" * navigation_count
        return os.path.join(root_dir, back_navigation, filename)

    @staticmethod
    def get_json_data(json_path: str) -> dict[str, list[str]]:
        data: dict[str, list[str]] = {}
        try:
            with open(json_path, mode="r") as jsonfile:
                data = json.load(jsonfile)
                return data
        except json.JSONDecodeError:
            return data

    @staticmethod
    def save_json_data(data: dict[str, list[str]], json_path: str):
        with open(json_path, mode="w") as jsonfile:
            return json.dump(data, jsonfile)
