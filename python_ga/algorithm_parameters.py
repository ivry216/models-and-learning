class MainAlgorithmParameters:

    def __init__(self, population_size, generations_number, dimension):
        self._size = population_size
        self._generations = generations_number
        self._dimension = dimension

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def generations(self):
        return self._generations

    @generations.setter
    def generations(self, value):
        self._generations = value

    @property
    def dimension(self):
        return self._dimension

    @dimension.setter
    def dimension(self, value):
        self._dimension = value
