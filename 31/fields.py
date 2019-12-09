from abc import ABC, abstractmethod
from validators import TextValidator, IntegerValidator

class AbstractField(ABC):

    @abstractmethod
    def __init__(self, validators): pass

    @abstractmethod
    def is_valid(self, value): pass


class CharField(AbstractField):

    def __init__(self, validators=None):
        self.default_validators = [TextValidator(0, 999)]
        self.all_validators = self.default_validators
        if isinstance(validators, list) and validators:
            self.all_validators += validators

    def is_valid(self, value):
        return all(item.is_valid(value) for item in self.all_validators)




class TextField(AbstractField):

    def __init__(self, validators=None):
        self.default_validators = [TextValidator(1001, 3000)]
        self.all_validators = self.default_validators
        if isinstance(validators, list) and validators:
            self.all_validators += validators

    def is_valid(self, value):
        return all(item.is_valid(value) for item in self.all_validators)
        # for i in self.all_validators:
        #     i.is_valid(value)


class IntegerField(AbstractField):

    def __init__(self, validators=None):
        self.default_validators = [IntegerValidator(128, 1024)]
        self.all_validators = self.default_validators
        if isinstance(validators, list) and validators:
            self.all_validators += validators

    def is_valid(self, value):
        return all(item.is_valid(value) for item in self.all_validators)
        # for i in self.all_validators:
        #     i.is_valid(value)
