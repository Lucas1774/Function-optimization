class Constants:
    _FILE_PATH = "input.xls"
    _INDEXES = {
        "variante-1": {
            "POPULATION": [[5, 2], [14, 14]],
            "RANDOM_NUMBERS": [[3, 17], [34, 21]],
        },
        "variante-2": {
            "POPULATION": [[5, 2], [20, 8]],
            "RANDOM_NUMBERS": [[3, 11], [34, 15]],
        },
    }

    @property
    def FILE_PATH(self):
        return self._FILE_PATH

    @property
    def INDEXES(self):
        return self._INDEXES
