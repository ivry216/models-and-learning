class SelectionParameters:

    def __init__(self, selection_type, tournament_size):
        self._type = selection_type
        self._tournament_size = tournament_size

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def tournament_size(self):
        return self._tournament_size

    @tournament_size.setter
    def tournament_size(self, value):
        self._tournament_size = value
