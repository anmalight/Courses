# !!!!
import datetime


class HumanAge:

    def __init__(self, b_day):
        self.b_day = b_day
        self.valid_b_day = self.validate(b_day)
        self.date_of_birth = self.str_to_datetime()
        self.date_now = datetime.datetime.now(tz=None)

    @staticmethod
    def validate(b_day):
        try:
            datetime.datetime.strptime(b_day, '%d-%m-%Y')
            return b_day
        except Exception as e:
            print(e)

    def str_to_datetime(self):
        date_of_birth = datetime.datetime.strptime(self.b_day, '%d-%m-%Y')
        return date_of_birth

    @property
    def age(self):
        if self.date_of_birth <= self.date_now:
            age = self.date_now.year - self.date_of_birth.year - \
                  ((self.date_now.month, self.date_now.day) < (self.date_of_birth.month, self.date_of_birth.day))
            return f"{age} year(s)"
        else:
            raise Exception("You have not yet been born")


human = HumanAge('07-12-1999')
# human = HumanAge('07-12-2055')
print(human.age)
