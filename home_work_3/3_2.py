# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in 4 out [2, 5, 8, 10] [20, 40]
# in 5 out [2, 2, 4, 8, 8] [16, 16, 4]

from random import sample

def list_ran_num(len_list):
    if len_list < 0:
        len_list = -len_list

    new_list = sample(range(1, 10), len_list)
    return new_list

def mult_num_list(n_list: list):
    new_list = []
    len_list = len(n_list)

    for k in range(len_list // 2):
        new_list.append(n_list[k] * n_list[len_list - k - 1])
    if len_list % 2:
        new_list.append(n_list[len_list // 2])
    return new_list

mult_list = list_ran_num(int(input("Количество чисел в списке: ")))
print(mult_list)
print(mult_num_list(mult_list)) 
