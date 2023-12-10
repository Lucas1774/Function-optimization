class DataManager:
    def print_data(data):
        for variant_name, variant_data in data.items():
            print(f"Variant: {variant_name}")
            for table_name, table_data in variant_data.items():
                print(f"Table: {table_name}")
                print(table_data)
