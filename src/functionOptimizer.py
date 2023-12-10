from dataSourceHandler import DataSourceHandler
from dataManager import DataManager


def main():
    file_path = DataSourceHandler.get_file_path()
    print(f"Attempting to read {file_path}")
    input_file = DataSourceHandler.read_excel_file(file_path)
    data = DataSourceHandler.parse(input_file)
    DataManager.print_data(data)


if __name__ == "__main__":
    main()
