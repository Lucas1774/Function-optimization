import sys
import pandas as pd
from constants import Constants


class DataSourceHandler:
    def read_excel_file(file_path):
        try:
            input_file = pd.read_excel(file_path, sheet_name=None)
            print(f"Successfully read {file_path}")
            return input_file
        except Exception as e:
            print(f"Failed to read {file_path}:")
            print(e)
            sys.exit(1)

    def get_file_path():
        constants = Constants()
        if len(sys.argv) == 2:
            return sys.argv[1]
        elif len(sys.argv) == 1:
            return constants.FILE_PATH
        else:
            print("Usage: functionOptimizer.py <file_name>")
            sys.exit(1)

    def parse(input_file):
        constants = Constants()
        processed_data = {}
        for sheet_name, sheet_data in input_file.items():
            if sheet_name not in processed_data:
                processed_data[sheet_name] = {}

            for table in constants.INDEXES[sheet_name]:
                start_row, start_col = constants.INDEXES[sheet_name][table][0]
                end_row, end_col = constants.INDEXES[sheet_name][table][1]

                table_df = sheet_data.iloc[
                    start_row - 1 : end_row - 1, start_col - 1 : end_col
                ]
                table_df.columns = sheet_data.values[
                    start_row - 2, start_col - 1 : end_col
                ].tolist()
                table_df.index = range(1, len(table_df.index) + 1)

                if table not in processed_data[sheet_name]:
                    processed_data[sheet_name][table] = []

                processed_data[sheet_name][table].append(table_df)
        return processed_data
