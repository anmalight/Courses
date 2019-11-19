class Temperatures:
    # This program gives the result only in whole degrees

    def _calculation(self, first):
        pass

    def from_celsius_to_fahrenheit(self, celsius):
        fahrenheit = str(round(celsius * (9 / 5) + 32))
        return fahrenheit+'F'
        # return fahrenheit 1

    def from_celsius_to_kelvin(self, celsius):
        kelvin = str(round(celsius+ 273.15))
        return kelvin + 'K'
        # return kelvin 2

    def from_fahrenheit_to_celsius(self, fahrenheit):
        celsius = str(round((fahrenheit - 32) * (5 / 9)))
        return celsius+'C'
        # return celsius 3

    def from_fahrenheit_to_kelvin(self, fahrenheit):
        kelvin = str(round((fahrenheit + 459.67)*(5/9)))
        return kelvin+"K"
        # return kelvin 4
        pass

    def from_kelvin_to_celsius(self, kelvin):
        celsius = str(round(kelvin - 273.15))
        return celsius+'C'
        # return celsius 5

    def from_kelvin_to_fahrenheit(self, kelvin):
        fahrenheit = str(round(kelvin - 459.67))
        return fahrenheit+"F"
        # return fahrenheit 6


instance1 = Temperatures().from_celsius_to_fahrenheit(23.89)
instance2 = Temperatures().from_celsius_to_kelvin(23.89)
instance3 = Temperatures().from_fahrenheit_to_celsius(75)
instance4 = Temperatures().from_fahrenheit_to_kelvin(75)
instance5 = Temperatures().from_kelvin_to_celsius(297.04)
instance6 = Temperatures().from_kelvin_to_fahrenheit(534.67)
print(instance1)
print(instance2)
print(instance3)
print(instance4)
print(instance5)
print(instance6)
