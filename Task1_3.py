# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

q = int(input('Введите значение четверти (от 1 до 4): '))

if q == 1:
    print('x > 0, y > 0')
if q == 2:
    print('x < 0, y > 0')
if q == 3:
    print('x < 0, y < 0')
if q == 4:
    print('x > 0 and y < 0')

