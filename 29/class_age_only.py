import datetime

class HumanAge:

    def __init__(self, b_day):
        self.date_now = datetime.datetime.now(tz=None)
        self.date_of_birth = self.validate_n_convert(b_day, self.date_now)

    @staticmethod
    def validate_n_convert(b_day, date_now):
        try:
            date_of_birth = datetime.datetime.strptime(b_day, '%d-%m-%Y')
            if date_of_birth >= date_now:
                raise Exception('Not relevant date!')
            else:
                return date_of_birth
        except Exception as e:
            print(e)

    @property
    def age(self):
        age = self.date_now.year - self.date_of_birth.year - \
              ((self.date_now.month, self.date_now.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return f"{age} year(s)"

    @property
    def intercal_years(self):
        number_of_years = 0
        for year in range(self.date_of_birth.year, self.date_now.year):
            if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
                number_of_years += 1
        return f"{number_of_years} leap years have passed"


human = HumanAge('07-12-1999')
# human = HumanAge('07-12-2020')
print(human.age)
print(human.intercal_years)
