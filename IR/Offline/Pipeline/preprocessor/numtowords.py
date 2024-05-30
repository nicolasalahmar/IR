import re

from num2words import num2words
from decimal import Decimal

from Offline.Pipeline.preprocessor.tokenize import to_tokens

unit_map = {
    # Length
    "km": "kilometer",
    '"': "inch",
    "m": "meter",
    "cm": "centimeter",
    "mm": "millimeter",
    "um": "micrometer (micron)",
    "nm": "nanometer",
    "pm": "picometer",
    "mi": "mile",
    "ft": "foot",
    "in": "inch",
    "yd": "yard",
    "angstrom": "angstrom",
    "nauticalmile": "nautical mile",
    "fathom": "fathom",

    # Mass
    "kg": "kilogram",
    "g": "gram",
    "mg": "milligram",
    "ug": "microgram",
    "ng": "nanogram",
    "pg": "picogram",
    "lb": "pound",
    "oz": "ounce",
    "t": "tonne (metric ton)",
    "cwt": "hundredweight",
    "qr": "quarter (quarter hundredweight)",
    "st": "stone",

    # Volume
    "l": "liter",
    "ml": "milliliter",
    "cl": "centiliter",
    "dl": "deciliter",
    "gal": "gallon",
    "qt": "quart",
    "pt": "pint",
    "floz": "fluid ounce",
    "cup": "cup",
    "tsp": "teaspoon",
    "tbsp": "tablespoon",
    "bbl": "barrel",

    # Time
    "s": "second",
    "min": "minute",
    "hr": "hour",
    "day": "day",
    "wk": "week",
    "mo": "month",
    "yr": "year",
    "ns": "nanosecond",
    "ps": "picosecond",
    "ms": "millisecond",

    # Temperature
    "celsius": "degrees Celsius",
    "fahrenheit": "degrees Fahrenheit",
    "k": "kelvin",

    # Area
    "km2": "square kilometer",
    "m2": "square meter",
    "cm2": "square centimeter",
    "mm2": "square millimeter",
    "ha": "hectare",
    "ac": "acre",
    "sqmi": "square mile",
    "sqft": "square foot",
    "sqin": "square inch",

    # Speed
    "kmh": "kilometers per hour",
    "fts": "feet per second",
    "mph": "miles per hour",
    "kt": "knot (nautical miles per hour)",

    # Force
    "n": "newton",
    "kn": "kilonewton",
    "mn": "meganewton",
    "lbf": "pound-force",
    "kip": "kip (force)",

    # Pressure
    "pa": "pascal",
    "kpa": "kilopascal",
    "mpa": "megapascal",
    "bar": "bar",
    "psi": "pounds per square inch",
    "mmHg": "millimeters of mercury",
    "atm": "atmosphere",

    # Energy
    "j": "joule",
    "kj": "kilojoule",
    "mj": "megajoule",
    "cal": "calorie",
    "kcal": "kilocalorie",
    "kwh": "kilowatt-hour",

    # Power
    "w": "watt",
    "kw": "kilowatt",
    "mw": "megawatt",
    "hp": "horsepower",

    # Electrical
    "v": "volt",
    "kv": "kilovolt",
    "mv": "megavolt",
    "a": "ampere",
    "ka": "kiloampere",
    "ma": "milliampere",
    "c": "coulomb",
    "f": "farad",
    "pf": "picofarad",
    "Ω": "ohm",
    "hz": "hertz",

    # Data
    "b": "byte",
    "kb": "kilobyte",
    "mb": "megabyte",
    "gb": "gigabyte",
}


def is_num(word):
    return word.replace('.', '', 1).isdigit()  # Allowing for decimals


def convert_num2words(tokens):
    result = []
    for idx, token in enumerate(tokens):
        if is_num(token):
            tokens[idx] = num2words(Decimal(str(token)), lang='en').replace(' ', '')
            result.append(tokens[idx])
        elif match := re.match(r'^(\d+\.\d+?)([a-zA-Z"]+)$', token):  # if float has (.) and unit
            value, unit = match.groups()
            if unit in unit_map:
                converted_unit = num2words(Decimal(value), lang='en').replace(' ', '') + ' ' + unit_map[unit]
                tokens[idx] = converted_unit
            result = result + to_tokens(tokens[idx])
        elif re.match(r'^\d+/\d+[a-zA-Z"]*$', token):    # if float has (/) and unit
            fraction, unit = re.match(r'^(\d+/\d+)([a-zA-Z"]*)$', token).groups()
            numerator, denominator = fraction.split('/')
            converted_fraction = num2words(int(numerator), lang='en').replace(' ', '') + 'slash' + num2words(
                int(denominator), lang='en').replace(' ', '')
            if unit:
                tokens[idx] = converted_fraction + ' ' + unit_map.get(unit, unit)
            else:
                tokens[idx] = converted_fraction
            result = result + to_tokens(tokens[idx])
        else:
            result.append(token)
    return result
