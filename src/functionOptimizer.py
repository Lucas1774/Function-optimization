from dataManagerV1 import DataManagerV1
from dataManagerV2 import DataManagerV2
from dataSourceHandler import DataSourceHandler
from excelData import ExcelData


def main():
    file_path = DataSourceHandler.get_file_path()
    print(f"Attempting to read {file_path}")
    input_file = DataSourceHandler.read_excel_file(file_path)

    print("-------------Imported data-------------")
    data = ExcelData(input_file)
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


if __name__ == "__main__":
    main()
