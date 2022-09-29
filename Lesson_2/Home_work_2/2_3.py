# * 4. Напишите программу, которая принимает на вход 2 числа. 
# Задайте список из N элементов, заполненных числами 
# из промежутка [-N, N]. Найдите произведение элементов на 
# указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

pos_1 = int(input())
pos_2 = int(input())
scope = int(input())
line = []
if pos_1 > (scope * 2 + 1) or pos_2 > (scope * 2 + 1):
    print('Exceeding the range!')
else:
    for i in range(-scope, scope+1):
        line.append(i)
    print(line[pos_1 - 1] * line[pos_2 - 1])



