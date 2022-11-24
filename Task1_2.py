# Напишите программу для проверки 
# истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат

def inputPredicates():
    xyz = ["X", "Y", "Z"]
    list = []
    for i in range(3):
        list.append(input(f"Введите значение {xyz[i]}: "))
    return list


def checkPredicates(xyz):
    left = not (xyz[0] or xyz[1] or xyz[2])
    right = not xyz[0] and not xyz[1] and not xyz[2]
    result = left == right
    return result


xyz = inputPredicates()

if checkPredicates(xyz) == True:
    print('True')
else:
    print('False')