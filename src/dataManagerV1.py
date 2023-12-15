import pandas as pd
from constants import Constants
from dataManagerInterface import IDataManager
from excelData import ExcelData


class DataManagerV1(IDataManager):
    @staticmethod
    def print(data: ExcelData):
        print(data.get_population("variante-1"))
        print(data.get_random_numbers("variante-1"))
        print(data.get_population("variante-2"))
        print(data.get_random_numbers("variante-2"))

    @staticmethod
    def do_selection(data: ExcelData):
        population_data = data.get_population("variante-1")

        adequation_value_sum = population_data["f.adecuación"].sum()
        selection_data = pd.DataFrame(
            {
                "individuals": population_data["individuo"],
                "selection probability": (
                    population_data["f.adecuación"] / adequation_value_sum
                ),
                "cumulative selection probability": (
                    population_data["f.adecuación"] / adequation_value_sum
                ).cumsum(),
            }
        )

        selected_individuals_data = []
        for _ in range(8):
            random_number = data.get_next_random("variante-1", "de 0 a 1")
            index = (
                selection_data["cumulative selection probability"] > random_number
            ).idxmax()

            selected_individual = selection_data.loc[index, "individuals"]
            selected_individuals_data.append(selected_individual)

        selected_individuals = pd.DataFrame(
            {"Selected Individuals": selected_individuals_data}
        )
        selected_individuals.index = range(1, len(selected_individuals) + 1)
        data.set_selected_individuals("variante-1", selected_individuals)

    @staticmethod
    def do_cross(data: ExcelData):
        constants = Constants()
        selected_individuals = data.get_selected_individuals("variante-1")
        pairs = [
            (
                selected_individuals.loc[i, "Selected Individuals"],
                selected_individuals.loc[i + 1, "Selected Individuals"],
            )
            for i in range(1, len(selected_individuals) + 1, 2)
        ]

        is_crossing_array = [
            data.get_next_random("variante-1", "de 0 a 1") < constants.CROSS_PROBABILITY
            for _ in range(len(pairs))
        ]
        index_of_first_crossing = [
            0
            if not is_crossing
            else data.get_next_random("variante-1", "de 1 a 10") + 1
            for is_crossing in is_crossing_array
        ]
        crossing_by_pairs = pd.DataFrame(
            {"Pairs": pairs, "First Chromosome": index_of_first_crossing}
        )
        crossing_by_pairs.index = range(1, len(crossing_by_pairs) + 1)
        data.set_crossing_by_pairs("variante-1", crossing_by_pairs)

    @staticmethod
    def do_next_generation(data: ExcelData):
        population_data = data.get_population("variante-1")
        crossing_by_pairs = data.get_crossing_by_pairs("variante-1")

        new_generation_data = []

        for _, row in crossing_by_pairs.iterrows():
            first_chromosome = row["First Chromosome"]
            first_parent = row["Pairs"][0]
            second_parent = row["Pairs"][1]

            first_child = []
            second_child = []

            for i in range(1, len(population_data.columns) - 1):
                if i < first_chromosome or first_chromosome == 0:
                    first_child.append(population_data.iloc[first_parent - 1, i])
                    second_child.append(population_data.iloc[second_parent - 1, i])
                else:
                    first_child.append(population_data.iloc[second_parent - 1, i])
                    second_child.append(population_data.iloc[first_parent - 1, i])

            new_generation_data.append(first_child)
            new_generation_data.append(second_child)

        new_generation = pd.DataFrame(
            new_generation_data, columns=population_data.columns[1:-1]
        )
        new_generation.insert(0, "Individual", range(1, len(new_generation) + 1), True)
        new_generation.index = range(1, len(new_generation) + 1)

        data.set_next_generation("variante-1", new_generation)

    def do_mutation(data: ExcelData):
        constants = Constants()
        next_generation = data.get_next_generation("variante-1")

        is_mutating_array = [
            data.get_next_random("variante-1", "de 0 a 1")
            < constants.MUTATION_PROBABILITY
            for _ in range(len(next_generation.index))
        ]

        mutating_genes_array = [
            (0, 0)
            if not is_mutating
            else (
                data.get_next_random("variante-1", "de 1 a 10") + 1,
                data.get_next_random("variante-1", "de 1 a 10") + 1,
            )
            for is_mutating in is_mutating_array
        ]

        mutated_genes = pd.DataFrame(
            {
                "Individuals": next_generation.index,
                "Mutated Genes": mutating_genes_array,
            }
        )
        mutated_genes.index = range(1, len(mutated_genes) + 1)

        data.set_mutated_genes("variante-1", mutated_genes)

    def do_next_generation_finish(data: ExcelData):
        next_generation = data.get_next_generation("variante-1")
        mutated_genes = data.get_mutated_genes("variante-1")

        new_generation_mutated_data = []

        for _, row in mutated_genes.iterrows():
            individual = row["Individuals"]
            mutated_gene = row["Mutated Genes"]

            if mutated_gene == (0, 0):
                new_generation_mutated_data.append(
                    next_generation.loc[individual].values[1:]
                )
            else:
                individual_data = next_generation.loc[individual].values[1:]
                g1, g2 = mutated_gene
                individual_data[g1 - 1], individual_data[g2 - 1] = (
                    individual_data[g2 - 1],
                    individual_data[g1 - 1],
                )
                new_generation_mutated_data.append(individual_data)

        new_generation_mutated = pd.DataFrame(
            new_generation_mutated_data, columns=next_generation.columns[1:]
        )
        new_generation_mutated.insert(
            0, "Individual", range(1, len(new_generation_mutated) + 1), True
        )
        new_generation_mutated.index = range(1, len(new_generation_mutated) + 1)

        data.set_next_generation_mutated("variante-1", new_generation_mutated)

    def do_replacement(data: ExcelData):
        population_data = data.get_population("variante-1")
        next_generation_mutated = data.get_next_generation_mutated("variante-1")

        next_generation_mutated["f.adecuación"] = None
        best_parent = population_data.loc[
            population_data["individuo"] == population_data["f.adecuación"].idxmax()
        ]
        best_parent.columns.values[0] = "Individual"
        next_generation_mutated = pd.concat(
            [next_generation_mutated, best_parent], ignore_index=True
        )

        data.set_next_generation_finished("variante-1", next_generation_mutated)
