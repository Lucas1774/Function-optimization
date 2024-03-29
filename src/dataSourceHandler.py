import sys
from typing import Dict
import pandas as pd
import xlwings as xw
from constants import Constants


class DataSourceHandler:
    @staticmethod
    def read_excel_file(file_path: str) -> Dict[str, pd.DataFrame]:
        try:
            input_file = pd.read_excel(file_path, sheet_name=None)
            print(f"Successfully read {file_path}")
            return input_file
        except Exception as e:
            print(f"Failed to read {file_path}:")
            print(e)
            sys.exit(1)

    @staticmethod
    def write_excel_file(
        file_path: str,
        sheet_name: str,
        data: pd.DataFrame,
        start_row: int,
        start_col: int,
    ):
        try:
            with xw.App() as app:
                wb = app.books.open(file_path)
                values = data.values
                rows = 9 if sheet_name == "variante-1" else 10

                for row_index in range(rows):
                    row = values[row_index]
                    for column_index, value in enumerate(row[1:-1]):
                        cell = wb.sheets[sheet_name].cells(
                            start_row + row_index, start_col + column_index
                        )
                        cell.value = value  # Corrected assignment

                wb.save()
                wb.close()
            print(f"Successfully wrote {file_path}")

        except Exception as e:
            print(f"Failed to read {file_path}:")
            print(e)
            sys.exit(1)

    @staticmethod
    def get_file_path() -> str:
        constants = Constants()
        if len(sys.argv) == 2:
            return sys.argv[1]
        elif len(sys.argv) == 1:
            return constants.FILE_PATH
        else:
            print("Usage: functionOptimizer.py <file_name>")
            sys.exit(1)

    @staticmethod
    def parse(
        input_file: Dict[str, pd.DataFrame]
    ) -> Dict[str, Dict[str, pd.DataFrame]]:
        constants = Constants()
        processed_data = {}

        for sheet_name, sheet_data in input_file.items():
            if sheet_name not in processed_data:
                processed_data[sheet_name] = {}

            for table in constants.INDEXES[sheet_name]:
                if table != "GENERATOR":
                    start_row, start_col = constants.INDEXES[sheet_name][table][0]
                    end_row, end_col = constants.INDEXES[sheet_name][table][1]

                    table_df = pd.DataFrame(
                        sheet_data.iloc[
                            start_row - 1 : end_row - 1, start_col - 1 : end_col
                        ]
                    )
                    table_df.columns = sheet_data.values[
                        start_row - 2, start_col - 1 : end_col
                    ].tolist()
                    table_df.index = range(1, len(table_df.index) + 1)

                    processed_data[sheet_name][table] = table_df

        return processed_data

    def parse_next_gen(
        variant: str, input_file: Dict[str, pd.DataFrame], current: pd.DataFrame
    ) -> pd.DataFrame:
        constants = Constants()
        start_row, start_col = constants.INDEXES[variant]["GENERATOR"][0]
        end_row, end_col = constants.INDEXES[variant]["GENERATOR"][1]

        table_df = pd.DataFrame(
            input_file[variant].iloc[start_row - 1 : end_row, start_col : end_col + 1]
        )
        if variant == "variante-2":
            best = table_df.sort_values(by=table_df.columns[-1], ascending=False).head(
                5
            )
            table_df = pd.concat([table_df, best])

        table_df.insert(0, "individuo", range(1, len(table_df) + 1), True)
        table_df.index = current.index
        table_df.columns = current.columns
        table_df.rename(columns={"Individual": "individuo"}, inplace=True)

        return table_df
