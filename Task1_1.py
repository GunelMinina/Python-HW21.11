# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('Введите число от 1 до 7, обозначающее день недели: ')
i = int(input())
if i == 6 or i == 7:
    print('Выходной день')
else:
    print('Рабочий день')
