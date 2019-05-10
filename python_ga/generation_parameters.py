class GenerationParameters:

    def __init__(self, generation_type):
        self._type = generation_type

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
