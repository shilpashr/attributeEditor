class RWAValidationException(Exception):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return repr(self.val)

class SimpleEXception(Exception):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return repr(self.val)



