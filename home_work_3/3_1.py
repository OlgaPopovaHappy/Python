# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in 5 out [10, 2, 3, 8, 9] 22
# in 4 out [4, 2, 4, 9] 8

from random import sample

def list_ran_num(len_list):
    if len_list < 0:
        len_list = -len_list
    new_list = sample(range(0, 10), len_list)
    print(new_list)
    return new_list

def sum_odd_num(n_list):
    sum = 0
    for i in range(len(n_list)):
        if i % 2 == 0:
            sum += n_list[i]
    return sum

my_list = int(input('Количество чисел в списке: '))
print(f'Сумму элементов, стоящих на нечётных позициях = {sum_odd_num(list_ran_num(my_list))}')