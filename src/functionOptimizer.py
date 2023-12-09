import sys
import pandas as pd
from constants import Constants


def read_excel_file(file_path):
    try:
        input_file = pd.read_excel(file_path)
        print(f"Successfully read {file_path}")
        return input_file
    except Exception as e:
        print(f"Failed to read {file_path}:")
        print(e)
        sys.exit(1)


def get_file_path():
    if len(sys.argv) == 2:
        return sys.argv[1]
    elif len(sys.argv) == 1:
        return constants.FILE_PATH
    else:
        print("Usage: functionOptimizer.py <file_name>")
        sys.exit(1)


def main():
    file_path = get_file_path()
    print(f"Attempting to read {file_path}")

    input_file = read_excel_file(file_path)
    print(input_file)


if __name__ == "__main__":
    constants = Constants()
    main()
