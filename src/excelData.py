from itertools import cycle
from typing import Dict
from pandas import DataFrame
from dataSourceHandler import DataSourceHandler


class ExcelData:
    def __init__(self, input_file: Dict[str, DataFrame]):
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

    def set_data(self, variant: str, input_file: Dict[str, DataFrame]):
        self.data[variant]["POPULATION"] = DataSourceHandler.parse_next_gen(
            variant, input_file, self.data[variant]["POPULATION"]
        )

    def get_population(self, variant: str) -> DataFrame:
        return self.data[variant]["POPULATION"]

    def get_random_numbers(self, variant: str) -> DataFrame:
        return self.data[variant]["RANDOM_NUMBERS"]

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

    def set_mutated_genes(self, variant: str, mutated_genes: DataFrame):
        self.data[variant]["MUTATED_GENES"] = mutated_genes

    def get_mutated_genes(self, variant: str) -> DataFrame:
        return self.data[variant]["MUTATED_GENES"]

    def set_next_generation_mutated(
        self, variant: str, next_generation_mutated: DataFrame
    ):
        self.data[variant]["NEXT_GENERATION_MUTATED"] = next_generation_mutated

    def get_next_generation_mutated(self, variant: str) -> DataFrame:
        return self.data[variant]["NEXT_GENERATION_MUTATED"]

    def set_next_generation_finished(
        self, variant: str, next_generation_finished: DataFrame
    ):
        self.data[variant]["NEXT_GENERATION_FINISHED"] = next_generation_finished

    def get_next_generation_finished(self, variant: str) -> DataFrame:
        return self.data[variant]["NEXT_GENERATION_FINISHED"]
