# unit_converter.py
# Модуль переводит значения из одних единиц в другие.
# Каждая функция принимает число и возвращает число.

def celsius_to_fahrenheit(celsius):
    """Перевод градусов Цельсия в градусы Фаренгейта.
    Формула: F = C * 9/5 + 32
    """
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """Перевод градусов Фаренгейта в градусы Цельсия.
    Формула: C = (F - 32) * 5/9
    """
    return (fahrenheit - 32) * 5 / 9


def km_to_miles(km):
    """Километры в мили. 1 км ≈ 0.621371 мили."""
    return km * 0.621371


def miles_to_km(miles):
    """Мили в километры. 1 миля ≈ 1.609344 км."""
    return miles * 1.609344


def kg_to_pounds(kg):
    """Килограммы в фунты. 1 кг ≈ 2.20462 фунта."""
    return kg * 2.20462


def pounds_to_kg(pounds):
    """Фунты в килограммы. 1 фунт ≈ 0.453592 кг."""
    return pounds * 0.453592


def convert(value, from_unit, to_unit):
    """Универсальный перевод по названиям единиц.
    from_unit и to_unit — строки: 'C', 'F', 'km', 'mi', 'kg', 'lb'.
    Если перевод не поддерживается — выбрасываем ошибку.
    """
    # Собираем все поддерживаемые пары в словарь.
    # Ключ — (откуда, куда), значение — функция перевода.
    converters = {
        ("C", "F"): celsius_to_fahrenheit,
        ("F", "C"): fahrenheit_to_celsius,
        ("km", "mi"): km_to_miles,
        ("mi", "km"): miles_to_km,
        ("kg", "lb"): kg_to_pounds,
        ("lb", "kg"): pounds_to_kg,
    }

    # Если такой пары нет — сообщаем об ошибке.
    key = (from_unit, to_unit)
    if key not in converters:
        raise ValueError(f"Перевод {from_unit} -> {to_unit} не поддерживается")

    # Нашли функцию — вызываем её с нашим значением.
    return converters[key](value)
