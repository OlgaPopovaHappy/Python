# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in 88 out 1011000
# in 11 out 1011

def decimal_binary(num):
    if num == 0:
        return print(num)
    elif num != 1:
        decimal_binary(num // 2)
    print(num % 2, end="")

decimal_binary(int(input('Введите число: ')))
print()