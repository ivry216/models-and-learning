import numpy as np


class GeneticAlgorithm:

    population = None
    fitness = None

    best_value = None
    best_alternative = None

    def __init__(self, parameters, problem):
        self._parameters = parameters
        self._problem = problem

    def generate(self):
        if self._parameters.generation.type == 'uniform':
            self.population = np.random.randint(2, size=(self._parameters.algorithm.size,
                                                         self._parameters.algorithm.dimension))
        self.fitness = self._problem.evaluate(self.population)

    def perform_select(self):
        if self._parameters.selection.type == 'tournament':
            numbers = np.arange(self._parameters.algorithm.size)
            np.random.shuffle(numbers)
            first_parents_inds = numbers[:self._parameters.selection.tournament_size]
            second_parents_inds = numbers[self._parameters.selection.tournament_size:
                                          2*self._parameters.selection.tournament_size]
            first_parent = np.argmax(np.take(self.fitness, first_parents_inds))
            second_parent = np.argmax(np.take(self.fitness, second_parents_inds))
            return first_parents_inds[first_parent], second_parents_inds[second_parent]
        return None

    def perform_crossover(self, first_index, second_index):
        offspring = np.copy(self.population[first_index])
        indices_to_get = np.random.randint(2, self._parameters.algorithm.dimension)
        offspring[indices_to_get == 1] = self.population[second_index][indices_to_get == 1]
        return offspring

    def perform_mutation(self, offspring):
        indices_to_mutate = np.random.choice(2, self._parameters.algorithm.dimension,
                                             p=[1 - self._parameters.mutation.probability, self._parameters.mutation.probability])
        offspring[indices_to_mutate == 1] = offspring[indices_to_mutate == 1] + 1
        offspring = np.remainder(offspring, 2)
        return offspring

    def perform_next(self):
        trial_population = np.zeros(shape=(self._parameters.algorithm.size, self._parameters.algorithm.dimension))
        for i in range(0, self._parameters.algorithm.size):
            parents_inds = self.perform_select()
            offspring = self.perform_crossover(parents_inds[0], parents_inds[1])
            mutant = self.perform_mutation(offspring)
            trial_population[:,i] = mutant
        self.population = trial_population
        self.fitness = self._problem.evaluate(self.population)

    def run(self):
        self.generate()
        best_alternative_index = np.argmax(self.fitness)
        self.best_value = self.fitness[best_alternative_index]
        self.best_alternative = self.population[:, best_alternative_index]
        for i in range(0, self._parameters.algorithm.generations):
            self.perform_next()
            best_alternative_index = np.argmax(self.fitness)
            self.best_value = self.fitness[best_alternative_index]
            self.best_alternative = self.population[:, best_alternative_index]
