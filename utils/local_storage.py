from data.storage import Storage
from utils.helper import Helper
from utils.savable import Savable


class LocalStorage:
    @staticmethod
    def _save_object(obj: Savable, key: str, storage: Storage):
        storage_path: str = Helper.get_filepath(storage.value)
        data: dict[str, list[str]] = Helper.get_json_data(storage_path)
        value = data.get(key, [])
        obj.save_to_location(location=value)
        data[key] = value
        Helper.save_json_data(data, storage_path)

    @staticmethod
    def save(obj: Savable, key: str, storage: Storage):
        LocalStorage._save_object(obj, key, storage)

    @staticmethod
    def search(query: str, storage: Storage) -> list[str]:
        datapath = Helper.get_filepath(storage.value)
        data = Helper.get_json_data(datapath)
        return data.get(query, [])

    @staticmethod
    def clear_storage(storage: Storage) -> None:
        storage_path: str = Helper.get_filepath(storage.value)
        Helper.save_json_data({}, storage_path)
