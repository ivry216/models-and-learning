class GeneticAlgorithmParameters:

    def __init__(self, algorithm, generation, selection, crossover, mutation):
        self._algorithm = algorithm
        self._generation = generation
        self._selection = selection
        self._crossover = crossover
        self._mutation = mutation

    @property
    def algorithm(self):
        return self._algorithm

    @algorithm.setter
    def algorithm(self, value):
        self._algorithm = value

    @property
    def generation(self):
        return self._generation

    @generation.setter
    def generation(self, value):
        self._generation = value

    @property
    def selection(self):
        return self._selection

    @selection.setter
    def selection(self, value):
        self._selection = value

    @property
    def crossover(self):
        return self._crossover

    @crossover.setter
    def crossover(self, value):
        self._crossover = value

    @property
    def mutation(self):
        return self._mutation

    @mutation.setter
    def mutation(self, value):
        self._mutation = value
