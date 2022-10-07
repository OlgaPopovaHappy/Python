# 1. Вычислить число c заданной точностью d
# in 
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000
# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
# out
# 8.988

from decimal import Decimal

def dec_i_mal(number, point):
    number = Decimal(n)
    print(number.quantize(Decimal(point)))
    return number

n = input('Число: ')
p = input('Требуемая точность: ')
dec_i_mal(n, p)

 