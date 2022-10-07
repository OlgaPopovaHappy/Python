# 2. Задайте натуральное число N. Напишите программу, которая составит список простых 
# множителей числа N.
# in 54  out [2, 3, 3, 3]
# in 9990 out [2, 3, 3, 3, 5, 37]
# in 650 out [2, 5, 5, 13]

def list_mult(num):
   i = 2
   line = []
   while i * i <= num:
       while num % i == 0:
           line.append(i)
           num = num // i
       i = i + 1
   if num > 1:
       line.append(num)
   return line

print(list_mult(int(input('Число: '))))