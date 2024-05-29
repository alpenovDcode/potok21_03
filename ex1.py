'''
- `Exception`: базовый класс для всех исключений.
- `ValueError`: возникает при некорректном значении.
- `TypeError`: возникает при несоответствии типов.
- `IndexError`: возникает при обращении к несуществующему индексу списка.
- `KeyError`: возникает при обращении к несуществующему ключу словаря.
- `IOError`: возникает при ошибках ввода-вывода.
'''

# базовая обработка исключений

# try:
#    x = int("abc")
# except ValueError:
#     print("Value error")

# else/finally

# try:
#     x = 1 / 1
# except ZeroDivisionError:
#     print("Деление на 0")
# else:
#     print("Ошибки нет")

# try:
#     x = 1 / 0
# except ZeroDivisionError:
#     print("Деление на 0")
# finally:
#     print("Ошибки нет")

# raise

# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError("Деление на ноль невозможно")
#     return a / b
#
# try:
#     result = divide(10, 0)
# except ZeroDivisionError as e:
#     print(e)

# class MyCustomError(Exception):
#     pass
#
# def do_smth(value):
#     if value < 0:
#         raise MyCustomError("Значение не может быть отрицательным")
#     print(value)
#
# try:
#     do_smth(10)
# except MyCustomError as e:
#     print(e)


# def do_smth(value):
#     try:
#         return 10 / value
#     except ZeroDivisionError:
#         print("Деление на ноль невозможно")
#         raise