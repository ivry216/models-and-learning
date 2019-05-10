import numpy as np


class AllOnesProblem:

    def __init__(self, dimension):
        self.dimension = dimension

    def evaluate(self, alternatives):
        return alternatives.sum(axis=0)
