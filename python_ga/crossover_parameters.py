class CrossoverParameters:

    def __init__(self, crossover_type):
        self._type = crossover_type

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
