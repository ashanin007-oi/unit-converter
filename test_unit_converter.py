# test_unit_converter.py
# Проверяем каждую функцию отдельно и универсальный convert.
# Для чисел с плавающей точкой сравниваем с допуском:
# абсолютная разница не должна превышать 0.01.

import pytest
from unit_converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    km_to_miles,
    miles_to_km,
    kg_to_pounds,
    pounds_to_kg,
    convert,
)


def test_celsius_to_fahrenheit():
    """0°C = 32°F, 100°C = 212°F — известные точки."""
    assert abs(celsius_to_fahrenheit(0) - 32) < 0.01
    assert abs(celsius_to_fahrenheit(100) - 212) < 0.01


def test_fahrenheit_to_celsius():
    """32°F = 0°C, 212°F = 100°C — те же точки обратно."""
    assert abs(fahrenheit_to_celsius(32) - 0) < 0.01
    assert abs(fahrenheit_to_celsius(212) - 100) < 0.01


def test_km_to_miles():
    """10 км ≈ 6.21371 мили."""
    assert abs(km_to_miles(10) - 6.21371) < 0.01


def test_miles_to_km():
    """10 миль ≈ 16.09344 км."""
    assert abs(miles_to_km(10) - 16.09344) < 0.01


def test_kg_to_pounds():
    """1 кг ≈ 2.20462 фунта."""
    assert abs(kg_to_pounds(1) - 2.20462) < 0.01


def test_pounds_to_kg():
    """1 фунт ≈ 0.453592 кг."""
    assert abs(pounds_to_kg(1) - 0.453592) < 0.01


def test_convert_supported():
    """Универсальная функция должна правильно выбрать перевод."""
    assert abs(convert(100, "C", "F") - 212) < 0.01
    assert abs(convert(10, "km", "mi") - 6.21371) < 0.01


def test_convert_unsupported():
    """Неподдерживаемая пара единиц — должна быть ошибка ValueError."""
    with pytest.raises(ValueError):
        convert(1, "kg", "km")  # килограммы в километры перевести нельзя
