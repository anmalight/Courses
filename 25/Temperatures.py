class Temperatures:
    # This program gives the result only in whole degrees

    def _calculation(self, first):
        return str(first)

    def from_celsius_to_fahrenheit(self, celsius):
        fahrenheit = round(celsius * (9 / 5) + 32)
        return f"{self._calculation(fahrenheit)}F"
        # return fahrenheit 1

    def from_celsius_to_kelvin(self, celsius):
        kelvin = round(celsius+ 273.15)
        return f"{self._calculation(kelvin)}K"
        # return kelvin 2

    def from_fahrenheit_to_celsius(self, fahrenheit):
        celsius = round((fahrenheit - 32) * (5 / 9))
        return f"{self._calculation(celsius)}C"
        # return celsius 3

    def from_fahrenheit_to_kelvin(self, fahrenheit):
        kelvin = round((fahrenheit + 459.67)*(5/9))
        return f"{self._calculation(kelvin)}K"
        # return kelvin 4

    def from_kelvin_to_celsius(self, kelvin):
        celsius = round(kelvin - 273.15)
        return f"{self._calculation(celsius)}C"
        # return celsius 5

    def from_kelvin_to_fahrenheit(self, kelvin):
        fahrenheit = round(kelvin - 459.67)
        return f"{self._calculation(fahrenheit)}F"
        # return fahrenheit 6

instance = Temperatures()
print(instance.from_celsius_to_fahrenheit(23.89))
print(instance.from_celsius_to_kelvin(23.89))
print(instance.from_fahrenheit_to_celsius(75))
print(instance.from_fahrenheit_to_kelvin(75))
print(instance.from_kelvin_to_celsius(297.04))
print(instance.from_kelvin_to_fahrenheit(534.67))
# print(dir(instance))
