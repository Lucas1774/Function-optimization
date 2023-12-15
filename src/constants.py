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

    _CROSS_PROBABILITY = 0.47
    _MUTATION_PROBABILITY = 0.29

    _NUMBER_OF_TOURNAMENTS = 4
    _CROSS_PROBABILITY_V2 = 0.73
    _MUTATION_PROBABILITY_V2 = 0.17
    _MIN_MUTATION_VALUE = -9
    _MAX_MUTATION_VALUE = 7

    @property
    def FILE_PATH(self):
        return self._FILE_PATH

    @property
    def INDEXES(self):
        return self._INDEXES

    @property
    def CROSS_PROBABILITY(self):
        return self._CROSS_PROBABILITY

    @property
    def MUTATION_PROBABILITY(self):
        return self._MUTATION_PROBABILITY
    
    @property
    def NUMBER_OF_TOURNAMENTS(self):
        return self._NUMBER_OF_TOURNAMENTS
    
    @property
    def CROSS_PROBABILITY_V2(self):
        return self._CROSS_PROBABILITY_V2
    
    @property
    def MUTATION_PROBABILITY_V2(self):
        return self._MUTATION_PROBABILITY_V2
    
    @property
    def MIN_MUTATION_VALUE(self):
        return self._MIN_MUTATION_VALUE
    
    @property
    def MAX_MUTATION_VALUE(self):
        return self._MAX_MUTATION_VALUE
