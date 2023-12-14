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

    def get_population(self, variant: str) -> DataFrame:
        return self.data[variant]["POPULATION"]

    def get_random_numbers(self, variant: str) -> DataFrame:
        return self.data[variant]["RANDOM_NUMBERS"]

    def set_selection_data(self, variant: str, selection_data: DataFrame):
        self.data[variant]["SELECTION"] = selection_data

    def get_selection_data(self, variant: str) -> DataFrame:
        return self.data[variant]["SELECTION"]

    def set_selected_individuals(self, variant: str, selected_individuals: DataFrame):
        self.data[variant]["SELECTED_INDIVIDUALS"] = selected_individuals

    def get_selected_individuals(self, variant: str) -> DataFrame:
        return self.data[variant]["SELECTED_INDIVIDUALS"]

    def set_crossing_by_pairs(self, variant: str, crossing_data: DataFrame):
        self.data[variant]["CROSSING_BY_PAIRS"] = crossing_data

    def get_crossing_by_pairs(self, variant: str) -> DataFrame:
        return self.data[variant]["CROSSING_BY_PAIRS"]

    def set_next_generation(self, variant: str, next_generation_data: DataFrame):
        self.data[variant]["NEXT_GENERATION"] = next_generation_data

    def get_next_generation(self, variant: str) -> DataFrame:
        return self.data[variant]["NEXT_GENERATION"]
