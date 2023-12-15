from abc import ABC, abstractmethod
from pandas import DataFrame


class IDataManager(ABC):
    @staticmethod
    @abstractmethod
    def do_selection(data: DataFrame):
        pass

    @staticmethod
    @abstractmethod
    def do_cross(data: DataFrame):
        pass

    @staticmethod
    @abstractmethod
    def do_next_generation(data: DataFrame):
        pass

    @staticmethod
    @abstractmethod
    def do_mutation(data: DataFrame):
        pass

    @staticmethod
    @abstractmethod
    def do_next_generation_finish(data: DataFrame):
        pass

    @staticmethod
    @abstractmethod
    def do_replacement(data: DataFrame):
        pass
