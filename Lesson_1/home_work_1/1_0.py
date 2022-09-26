# 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# - 6 -> да
# - 7 -> да
# - 1 -> нет

workday = [1, 2, 3, 4, 5]
weekend = [6, 7]
n_week = int(input('Enter the number of the day of the week: '))

if n_week in workday:
    print('Workday')
elif n_week in weekend:
    print('Weekend')
else:
    print("It's not a day of the week!")



