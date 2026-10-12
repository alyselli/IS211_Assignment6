
class ConversionNotPossible(Exception):
    pass


def convert(fromUnit, toUnit, value):
    temperatures = ["Celsius", "Fahrenheit", "Kelvin"]
    distances = ["Miles", "Yards", "Meters"]

    if fromUnit == toUnit:
        if fromUnit in temperatures or fromUnit in distances:
            return float(value)
        raise ConversionNotPossible("Unknown unit")

    if fromUnit in temperatures and toUnit in temperatures:

        if fromUnit == "Celsius":
            celsius = value
        elif fromUnit == "Fahrenheit":
            celsius = (value - 32) * 5 / 9
        else:
            celsius = value - 273.15

        if toUnit == "Celsius":
            return float(celsius)
        elif toUnit == "Fahrenheit":
            return float(celsius * 9 / 5 + 32)
        else:
            return float(celsius + 273.15)

    elif fromUnit in distances and toUnit in distances:

        if fromUnit == "Miles":
            meters = value * 1609.344
        elif fromUnit == "Yards":
            meters = value * 0.9144
        else:
            meters = value

        if toUnit == "Miles":
            return float(meters / 1609.344)
        elif toUnit == "Yards":
            return float(meters / 0.9144)
        else:
            return float(meters)

    else:
        raise ConversionNotPossible(
            "Cannot convert between these units"
        )
