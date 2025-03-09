def caching_fibonacci():
    # Створюємо словник для кешування обчислених значень
    cache = {}
   
    def fibonacci(n):
        # Базові випадки
        if n <= 0:
            return 0
        if n == 1:
            return 1
       
        # Перевірка, чи значення вже є в кеші
        if n in cache:
            return cache[n]
       
        # Обчислення нового значення та збереження в кеш
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
   
    return fibonacci

# Створюємо екземпляр функції з кешуванням
fib = caching_fibonacci()

# Тестування
print(fib(10))
print(fib(15))
print(fib(4))