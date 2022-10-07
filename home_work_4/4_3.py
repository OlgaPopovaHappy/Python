# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности в том же порядке.
# in 7 out [4, 5, 3, 3, 4, 1, 2] [5, 1, 2]
# in -1 out Negative value of the number of numbers! []
# in 10 out [4, 4, 5, 5, 6, 2, 3, 0, 9, 4] [6, 2, 3, 0, 9]


from random import randint

def rand_list(l_list):
    if l_list < 0:
        print('Negative value of the number of numbers!')
        return []
    else:
        new_list = [randint(1, 10) for i in range(l_list)]
        print(new_list)
        return new_list

def non_repeating(n_list):
    z = []
    for i in range(len(n_list)):
        n_count = n_list.count(n_list[i])
        if n_count == 1:
            z.append(n_list[i])
    return z

in_list = int(input('Размер исходного списка: '))
print(non_repeating(rand_list(in_list)))
