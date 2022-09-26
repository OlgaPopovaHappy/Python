# 5. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве. 




x1 = float(input('Enter X1: '))
y1 = float(input('Enter Y1: '))
x2 = float(input('Enter X2: '))
y2 = float(input('Enter Y2: '))
 
print(round(((((x2-x1)**2) + ((y2-y1)**2))**0.5 ), 2))
