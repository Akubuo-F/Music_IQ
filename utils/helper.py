import json
import os
from dotenv import load_dotenv

from utils.savable import Savable


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
        file_path: str = Helper.get_filepath(json_path)
        with open(file_path, mode="r") as jsonfile:
            return json.load(jsonfile)

    @staticmethod
    def save_object(obj: Savable, key: str, json_path: str):
        data: dict[str, list[str]] = Helper.get_json_data(json_path)
        value = data.get(key, [])
        obj.save(location=value)
        data[key] = value

        with open(json_path, "w") as jsonfile:
            json.dump(data, jsonfile)
