
from conversions_refactored import convert, ConversionNotPossible

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


class TestRefactoredConversions(unittest.TestCase):

    def testTemperatureConversions(self):
        cases = [
            ("Celsius", "Fahrenheit", 100, 212),
            ("Celsius", "Kelvin", 0, 273.15),
            ("Fahrenheit", "Celsius", 32, 0),
            ("Fahrenheit", "Kelvin", 212, 373.15),
            ("Kelvin", "Celsius", 273.15, 0),
            ("Kelvin", "Fahrenheit", 373.15, 212)
        ]

        for fromUnit, toUnit, value, expected in cases:
            print(f"Testing {fromUnit} to {toUnit}")
            with self.subTest(fromUnit=fromUnit, toUnit=toUnit):
                self.assertAlmostEqual(
                    convert(fromUnit, toUnit, value), expected
                )

    def testDistanceConversions(self):
        cases = [
            ("Miles", "Yards", 1, 1760),
            ("Miles", "Meters", 1, 1609.344),
            ("Yards", "Miles", 1760, 1),
            ("Yards", "Meters", 1, 0.9144),
            ("Meters", "Miles", 1609.344, 1),
            ("Meters", "Yards", 0.9144, 1)
        ]

        for fromUnit, toUnit, value, expected in cases:
            print(f"Testing {fromUnit} to {toUnit}")
            with self.subTest(fromUnit=fromUnit, toUnit=toUnit):
                self.assertAlmostEqual(
                    convert(fromUnit, toUnit, value), expected
                )

    def testSameUnitConversions(self):
        units = [
            "Celsius", "Fahrenheit", "Kelvin",
            "Miles", "Yards", "Meters"
        ]

        for unit in units:
            print(f"Testing {unit} to {unit}")
            with self.subTest(unit=unit):
                self.assertEqual(
                    convert(unit, unit, 100), 100.0
                )

    def testInvalidConversions(self):
        cases = [
            ("Celsius", "Meters"),
            ("Miles", "Fahrenheit"),
            ("Kelvin", "Yards"),
            ("Meters", "Celsius"),
            ("Unknown", "Celsius")
        ]

        for fromUnit, toUnit in cases:
            print(f"Testing invalid conversion: {fromUnit} to {toUnit}")
            with self.subTest(fromUnit=fromUnit, toUnit=toUnit):
                with self.assertRaises(ConversionNotPossible):
                    convert(fromUnit, toUnit, 100)


if __name__ == "__main__":
    unittest.main(verbosity=2)


from conversions_refactored import convert, ConversionNotPossible

