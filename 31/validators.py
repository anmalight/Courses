from abc import ABC, abstractmethod


class AbstractValidator(ABC):

    @abstractmethod
    def __init__(self, min_length, max_length): pass

    @abstractmethod
    def is_valid(self, value): pass


class TextValidator(AbstractValidator):

    def __init__(self, min_length=16, max_length=256):
        self.min_length = min_length
        self.max_length = max_length

    def is_valid(self, value):
        if len(value) >= self.min_length and len(value) <= self.max_length:
            return True
        else:
            return False

# for_text_validator = TextValidator()
# print(for_text_validator.is_valid('xkmdczrebghjkuyte'))


class IntegerValidator(AbstractValidator):
    def __init__(self, min_length=32, max_length=1024):
        self.min_length = min_length
        self.max_length = max_length

    def is_valid(self, value):
        if value >= self.min_length and value <= self.max_length:
            return True
        else:
            return False


# for_integer_validator = IntegerValidator()
# print(for_integer_validator .is_valid(10))