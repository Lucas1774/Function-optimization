from dataManager import DataManager
from dataSourceHandler import DataSourceHandler
from excelData import ExcelData


def main():
    file_path = DataSourceHandler.get_file_path()
    print(f"Attempting to read {file_path}")
    input_file = DataSourceHandler.read_excel_file(file_path)

    print("-------------Imported data-------------")
    data = ExcelData(input_file)
    DataManager.print(data)
    print()

    print("-------------Selected individuals for variant-1-------------")
    DataManager.do_selection_variant_1(data)
    print(data.get_selected_individuals("variante-1"))
    print()

    print("-------------Crossing data for variant-1-------------")
    DataManager.do_cross_variant_1(data)
    print(data.get_crossing_by_pairs("variante-1"))
    print()

    print("-------------Next generation's genes-------------")
    DataManager.do_next_generation_variant_1(data)
    print(data.get_next_generation("variante-1"))
    print()


if __name__ == "__main__":
    main()
