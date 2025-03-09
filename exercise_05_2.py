import re
from typing import Callable

def generator_numbers(text: str):
    # Знаходимо всі числа в тексті за допомогою регулярного виразу
    numbers = re.findall(r'\d+\.\d+', text)
   
    # Перетворюємо знайдені числа в float
    profits = [float(num) for num in numbers]
   
    # Ініціалізація проміжної суми
    total_profit = 0.0
   
    # Викликаємо yield для повернення проміжних сум
    for profit in profits:
        total_profit += profit
        yield total_profit

def sum_profit(text: str, func: Callable[[str], float]) -> float:
    # Беремо лише останнє значення з генератора
    return list(func(text))[-1]

# Тестування
test_text = """Заработный доход працьовника складається з деклькох частин:
1000.01 як основний дохід,
додатковий додатковими надходженнями 27.45 і
324.00 доплата.
"""

total_income = sum_profit(test_text, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}")