import re
from typing import Callable

def generator_numbers(text: str):
    # Знаходимо всі числа в тексті, які мають пробіл перед собою
    numbers = re.findall(r'\s\d+\.\d+', text)

    # Перетворюємо значення чисел у float, прибираючи пробіл перед числом
    profits = [float(num.strip()) for num in numbers]

    # Використовуємо yield для повернення проміжних сум
    for profit in profits:
        yield profit

def sum_profit(text: str, func: Callable[[str], float]) -> float:
    # Обчислюємо загальну суму чисел
    total = 0.0
    for profit in func(text):
        total += profit
    return total

# Тестування
test_text = """Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, додатковий дохід 27.45 і 324.00 доплата."""
total_income = sum_profit(test_text, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}")