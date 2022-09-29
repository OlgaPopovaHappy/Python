# 3. Задайте список из n чисел, заполненный по формуле 
# (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13


n = int(input())
line = []
sum = 0
for i in range(n):
    line.append((1+1/n)**n)
    sum = sum + int(line[i])
print(sum)





