# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def inputCoord():
    xy = ["X", "Y"]
    list = []
    for i in range(2):
        list.append(int(input(f"Введите значение {xy[i]}: ")))
    return list

def getS(a, b):
    s = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return s

a = inputCoord()
b = inputCoord()

print(getS(a, b))
