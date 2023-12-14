from itertools import cycle
from typing import Dict
from pandas import DataFrame
from dataSourceHandler import DataSourceHandler


class ExcelData:
    def __init__(self, input_file: str):
        self.data = DataSourceHandler.parse(input_file)
        self.iterators = {}

    def get_next_random(self, variant: str, column_name: str) -> float:
        if variant not in self.iterators:
            self.iterators[variant] = {}

        if column_name not in self.iterators[variant]:
            column_values = self.data[variant]["RANDOM_NUMBERS"][column_name]
            self.iterators[variant][column_name] = cycle(column_values)

        next_value = next(self.iterators[variant][column_name])
        return next_value

    def get_data(self) -> Dict:
        return self.data

    def get_population(self, variant) -> DataFrame:
        return self.data[variant]["POPULATION"]

    def get_random_numbers(self, variant) -> DataFrame:
        return self.data[variant]["RANDOM_NUMBERS"]

    def set_selection_data(self, variant, data: DataFrame):
        self.data[variant]["SELECTION"] = data

    def get_selection_data(self, variant) -> DataFrame:
        return self.data[variant]["SELECTION"]

    def set_selected_individuals(self, variant, data: DataFrame):
        self.data[variant]["SELECTED_INDIVIDUALS"] = data

    def get_selected_individuals(self, variant) -> DataFrame:
        return self.data[variant]["SELECTED_INDIVIDUALS"]

    def set_crossing_by_pairs(self, variant, data: DataFrame):
        self.data[variant]["CROSSING_BY_PAIRS"] = data

    def get_crossing_by_pairs(self, variant) -> DataFrame:
        return self.data[variant]["CROSSING_BY_PAIRS"]

    def set_next_generation(self, variant, data: DataFrame):
        self.data[variant]["NEXT_GENERATION"] = data

    def get_next_generation(self, variant) -> DataFrame:
        return self.data[variant]["NEXT_GENERATION"]
