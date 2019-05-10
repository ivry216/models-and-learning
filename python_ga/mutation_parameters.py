class MutationParameters:

    def __init__(self, mutation_type, mutation_probability):
        self._type = mutation_type
        self._probability = mutation_probability

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def probability(self):
        return self._probability

    @probability.setter
    def probability(self, value):
        self._probability = value
