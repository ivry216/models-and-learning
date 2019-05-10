from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import StratifiedKFold
import threading
from multiprocessing.dummy import Pool as ThreadPool


class Problem:

    x = None
    y = None
    skf = None
    train_index = None
    test_index = None

    trains_x = None
    tests_x = None
    trains_y = None
    tests_y = None

    def __init__(self, number_of_splits):
        self._data = pd.DataFrame()
        self._filename = ""
        self._folds_number = number_of_splits

    def set_data(self, file_name_):
        self._data = pd.read_excel(file_name_)
        self.x = self._data.iloc[:, :-1]
        self.y = np.zeros(self._data.shape[0])
        self.y[self._data.iloc[:, -1] == 'chd'] = 1
        self.skf = StratifiedKFold(n_splits=self._folds_number, random_state=None, shuffle=True)
        skf_generator = self.skf.split(self.x, self.y)

        self.trains_x = []
        self.tests_x = []
        self.trains_y = []
        self.tests_y = []

        for train_index, test_index in skf_generator:
            self.trains_x.append(self.x.iloc[train_index, :])
            self.tests_x.append(self.x.iloc[test_index, :])
            self.trains_y.append(self.y[train_index])
            self.tests_y.append(self.y[test_index])

    def evaluate(self, population):

        number_of_individuals = population.shape[0]
        accuracy = np.zeros(number_of_individuals)

        for i in range(0, number_of_individuals):

            for j in range(self._folds_number):

                current_x_train = self.trains_x[j].iloc[i, population[i, :] == 1]
                current_x_test = self.tests_x[j].iloc[i, population[i, :] == 1]
                logit = LogisticRegression(penalty='l1', max_iter=500, C=1.0)
                y_prediction = logit.fit(current_x_train, np.ravel(self.trains_y[j])).predict(current_x_test)
                accuracy[i] = accuracy[i] + np.sum(y_prediction == self.tests_y[j]) / self.tests_y[j].size

        return accuracy / self._folds_number
