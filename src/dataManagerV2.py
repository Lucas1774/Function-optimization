import pandas as pd
from constants import Constants
from dataManagerInterface import IDataManager
from excelData import ExcelData


class DataManagerV2(IDataManager):
    @staticmethod
    def do_selection(data: ExcelData):
        constants = Constants()
        population_data = data.get_population("variante-2")
        tournament_data = []

        for _ in range(constants.NUMBER_OF_TOURNAMENTS):
            selected = []
            for _ in range(3):
                random_number = 0
                while random_number in selected or random_number == 0:
                    random_number = data.get_next_random("variante-2", "de 1 a 15")
                selected.append(random_number)

            winner = population_data.loc[selected, "f.adecuación"].idxmax()
            tournament_data.append(winner)

        selected_individuals = pd.DataFrame({"Selected Individuals": tournament_data})
        selected_individuals.index = range(1, len(selected_individuals) + 1)

        data.set_selected_individuals("variante-2", selected_individuals)

    @staticmethod
    def do_cross(data: ExcelData):
        constants = Constants()
        selected_individuals = data.get_selected_individuals("variante-2")
        pairs = [
            (
                selected_individuals.loc[i, "Selected Individuals"],
                selected_individuals.loc[i + 1, "Selected Individuals"],
            )
            for i in range(1, len(selected_individuals) + 1, 2)
        ]

        is_crossing_array = [
            data.get_next_random("variante-2", "de 0 a 1")
            < constants.CROSS_PROBABILITY_V2
            for _ in range(len(pairs))
        ]

        crossing_by_pairs = pd.DataFrame(
            {"Pairs": pairs, "Crossing": is_crossing_array}
        )
        crossing_by_pairs.index = range(1, len(crossing_by_pairs) + 1)
        data.set_crossing_by_pairs("variante-2", crossing_by_pairs)

    @staticmethod
    def do_next_generation(data: ExcelData):
        population_data = data.get_population("variante-2")
        crossing_by_pairs = data.get_crossing_by_pairs("variante-2")

        new_generation_data = []

        for _, row in crossing_by_pairs.iterrows():
            is_crossing = row["Crossing"]
            first_parent = row["Pairs"][0]
            second_parent = row["Pairs"][1]

            first_child = []
            second_child = []

            for i in range(1, len(population_data.columns) - 1):
                first_parent_gen = population_data.iloc[first_parent - 1, i]
                second_parent_gen = population_data.iloc[second_parent - 1, i]
                if not is_crossing:
                    first_child.append(population_data.iloc[first_parent - 1, i])
                    second_child.append(population_data.iloc[second_parent - 1, i])
                else:
                    first_child.append(
                        (second_parent_gen - first_parent_gen)
                        * data.get_next_random("variante-2", "de 0 a 1")
                        + first_parent_gen
                    )
                    second_child.append(
                        (second_parent_gen - first_parent_gen)
                        * data.get_next_random("variante-2", "de 0 a 1")
                        + first_parent_gen
                    )
            new_generation_data.append(first_child)
            new_generation_data.append(second_child)

        new_generation = pd.DataFrame(
            new_generation_data, columns=population_data.columns[1:-1]
        )
        new_generation.insert(0, "Individual", range(1, len(new_generation) + 1), True)
        new_generation.index = range(1, len(new_generation) + 1)

        data.set_next_generation("variante-2", new_generation)

    def do_mutation(data: ExcelData):
        constants = Constants()
        next_generation = data.get_next_generation("variante-2").copy()

        mutated_genes_data = {"Individual": [], "Mutated_Genes": []}

        for index, row in next_generation.iterrows():
            mutated_indices = []
            for i in range(1, len(row)):
                if (
                    data.get_next_random("variante-2", "de 0 a 1")
                    < constants.MUTATION_PROBABILITY_V2
                ):
                    mutation_value = (
                        constants.MAX_MUTATION_VALUE - constants.MIN_MUTATION_VALUE
                    ) * data.get_next_random(
                        "variante-2", "de 0 a 1"
                    ) + constants.MIN_MUTATION_VALUE
                    next_generation.at[
                        index, next_generation.columns[i]
                    ] = mutation_value
                    mutated_indices.append(i)

            mutated_genes_data["Individual"].append(index)
            mutated_genes_data["Mutated_Genes"].append(tuple(mutated_indices))

        mutated_genes = pd.DataFrame(mutated_genes_data)

        next_generation.index = range(1, len(next_generation) + 1)

        data.set_mutated_genes("variante-2", mutated_genes)
        data.set_next_generation_mutated("variante-2", next_generation)

    def do_next_generation_finish(data: ExcelData):
        pass

    def do_replacement(data: ExcelData):
        constants = Constants()
        population_data = data.get_population("variante-2")
        next_generation_mutated = data.get_next_generation_mutated("variante-2")
        next_generation_mutated["f.adecuación"] = None
        best_parents = population_data.sort_values(
            by="f.adecuación", ascending=False
        ).head(len(population_data) - constants.NUMBER_OF_TOURNAMENTS)
        best_parents.columns.values[0] = "Individual"

        next_generation_mutated = pd.concat(
            [next_generation_mutated, best_parents], ignore_index=True
        )

        data.set_next_generation_finished("variante-2", next_generation_mutated)
