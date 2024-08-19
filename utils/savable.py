from abc import ABC, abstractmethod


class Savable(ABC):
    """
    An abstract base class that defines the interface for objects that can be saved and loaded.

    Classes implementing this interface must provide methods for saving their state to a specified
    location and loading their state from a string or a dictionary representation.

    This interface may be implemented by various data classes, such as `Song` and `Artist`.
    """

    @abstractmethod
    def save(self, location: list[str]) -> None:
        """
        Saves the object to a specified location.

        Parameters:
            location (list[str]): A list representing the location where the object
                                  should be saved (e.g., a list that will contain
                                  the JSON string representation of the object).
        """
        ...

    @classmethod
    @abstractmethod
    def load_from_json_str(cls, object_str: str) -> "Savable":
        """
        Loads an instance of the implementing class from a JSON string.

        Parameters:
            object_str (str): A JSON string representation of the object.

        Returns:
            Savable: An instance of the implementing class.
        """
        ...

    @classmethod
    def load_from_dict(cls, data: dict) -> "Savable":
        """
        Loads an instance of the implementing class from a dictionary representation.

        Parameters:
            data (dict): A dictionary containing the object's data.

        Returns:
            Savable: An instance of the implementing class.
        """
        ...
