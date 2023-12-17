from dataManagerV1 import DataManagerV1
from dataManagerV2 import DataManagerV2
from dataSourceHandler import DataSourceHandler
from excelData import ExcelData
from constants import Constants


def main():
    def run():
        print("-------------Imported data-------------")
        DataManagerV1.print(data)
        print()

        print("-------------Selected individuals for variant-1-------------")
        DataManagerV1.do_selection(data)
        print(data.get_selected_individuals("variante-1"))
        print()

        print("-------------Crossing data for variant-1-------------")
        DataManagerV1.do_cross(data)
        print(data.get_crossing_by_pairs("variante-1"))
        print()

        print("-------------Next generation's genes for variant-1-------------")
        DataManagerV1.do_next_generation(data)
        print(data.get_next_generation("variante-1"))
        print()

        print("-------------Mutated genes for variant-1-------------")
        DataManagerV1.do_mutation(data)
        print(data.get_mutated_genes("variante-1"))
        print()

        print(
            "-------------Next generation's genes after mutation for variant-1-------------"
        )
        DataManagerV1.do_next_generation_finish(data)
        print(data.get_next_generation_mutated("variante-1"))
        print()

        print("-------------Next generation for variant-1-------------")
        DataManagerV1.do_replacement(data)
        print(data.get_next_generation_finished("variante-1"))
        print()

        print("-------------Selected individuals for variant-2-------------")
        DataManagerV2.do_selection(data)
        print(data.get_selected_individuals("variante-2"))
        print()

        print("-------------Crossing data for variant-2-------------")
        DataManagerV2.do_cross(data)
        print(data.get_crossing_by_pairs("variante-2"))
        print()

        print("-------------Next generation's genes for variant-2-------------")
        DataManagerV2.do_next_generation(data)
        print(data.get_next_generation("variante-2"))
        print()

        print("-------------Mutated genes for variant-2-------------")
        DataManagerV2.do_mutation(data)
        print(data.get_mutated_genes("variante-2"))
        print()

        print(
            "-------------Next generation's genes after mutation for variant-1-------------"
        )
        DataManagerV2.do_next_generation_finish(data)
        print(data.get_next_generation_mutated("variante-2"))
        print()

        print("-------------Next generation for variant-2-------------")
        DataManagerV2.do_replacement(data)
        print(data.get_next_generation_finished("variante-2"))
        print()

        print(f"Attempting to write variant-1 in {file_path}")
        DataSourceHandler.write_excel_file(
            file_path=file_path,
            sheet_name="variante-1",
            data=data.get_next_generation_finished("variante-1"),
            start_row=constants.INDEXES["variante-1"]["GENERATOR"][0][0] + 1,
            start_col=constants.INDEXES["variante-1"]["GENERATOR"][0][1] + 1,
        )
        print(f"Attempting to write variant-2 in {file_path}")
        DataSourceHandler.write_excel_file(
            file_path=file_path,
            sheet_name="variante-2",
            data=data.get_next_generation_finished("variante-2"),
            start_row=constants.INDEXES["variante-2"]["GENERATOR"][0][0] + 1,
            start_col=constants.INDEXES["variante-2"]["GENERATOR"][0][1] + 1,
        )

    constants = Constants()
    file_path = DataSourceHandler.get_file_path()

    for i in range(constants._NUMBER_OF_ITERATIONS):
        print(f"Attempting to read {file_path}")
        input_file = DataSourceHandler.read_excel_file(file_path)
        if i == 0:
            data = ExcelData(input_file)
        else:
            data.set_data("variante-1", input_file)
            data.set_data("variante-2", input_file)
        run()


if __name__ == "__main__":
    main()
