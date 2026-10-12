
import unittest
from conversions import (
    convertCelsiusToKelvin,
    convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius,
    convertFahrenheitToKelvin,
    convertKelvinToCelsius,
    convertKelvinToFahrenheit
)


class TestConversions(unittest.TestCase):

    def testCelsiusToKelvin(self):
        cases = [
            (0, 273.15),
            (100, 373.15),
            (-40, 233.15),
            (300, 573.15),
            (25, 298.15)
        ]
        for value, expected in cases:
            print(f"Testing {value} Celsius to Kelvin")
            with self.subTest(value=value):
                self.assertAlmostEqual(
                    convertCelsiusToKelvin(value), expected
                )

    def testCelsiusToFahrenheit(self):
        cases = [
            (0, 32),
            (100, 212),
            (-40, -40),
            (300, 572),
            (25, 77)
        ]
        for value, expected in cases:
            print(f"Testing {value} Celsius to Fahrenheit")
            with self.subTest(value=value):
                self.assertAlmostEqual(
                    convertCelsiusToFahrenheit(value), expected
                )

    def testFahrenheitToCelsius(self):
        cases = [
            (32, 0),
            (212, 100),
            (-40, -40),
            (572, 300),
            (77, 25)
        ]
        for value, expected in cases:
            print(f"Testing {value} Fahrenheit to Celsius")
            with self.subTest(value=value):
                self.assertAlmostEqual(
                    convertFahrenheitToCelsius(value), expected
                )

    def testFahrenheitToKelvin(self):
        cases = [
            (32, 273.15),
            (212, 373.15),
            (-40, 233.15),
            (572, 573.15),
            (77, 298.15)
        ]
        for value, expected in cases:
            print(f"Testing {value} Fahrenheit to Kelvin")
            with self.subTest(value=value):
                self.assertAlmostEqual(
                    convertFahrenheitToKelvin(value), expected
                )

    def testKelvinToCelsius(self):
        cases = [
            (273.15, 0),
            (373.15, 100),
            (233.15, -40),
            (573.15, 300),
            (298.15, 25)
        ]
        for value, expected in cases:
            print(f"Testing {value} Kelvin to Celsius")
            with self.subTest(value=value):
                self.assertAlmostEqual(
                    convertKelvinToCelsius(value), expected
                )

    def testKelvinToFahrenheit(self):
        cases = [
            (273.15, 32),
            (373.15, 212),
            (233.15, -40),
            (573.15, 572),
            (298.15, 77)
        ]
        for value, expected in cases:
            print(f"Testing {value} Kelvin to Fahrenheit")
            with self.subTest(value=value):
                self.assertAlmostEqual(
                    convertKelvinToFahrenheit(value), expected
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
