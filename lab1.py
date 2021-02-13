# Вариант 221

import random

list_X = []
list1 = []
list2 = []
list3 = []
list_A = []
list_Y = []

# Генерируем массив чисел
for i in range(8):
    list_X.append([random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)])
    list1.append(list_X[i][0])
    list2.append(list_X[i][1])
    list3.append(list_X[i][2])

print("X:", list_X)jdjdjdj
print()

# Генерируем коеффициенты
for i in range(4):
    list_A.append(random.randint(1, 10))
print("a:", list_A)
print()

# Считаем Y
not_y = 0
for i in range(len(list_X)):
    not_y = 0
    for j in range(len(list_X[i])):
        not_y += list_A[j + 1] * list_X[i][j]
    list_Y.append(not_y + list_A[0])
print("Y:", list_Y)
print()

# Считаем х0
list_x0 = []
list_x0.append((max(list1) + min(list1)) / 2)
list_x0.append((max(list2) + min(list2)) / 2)
list_x0.append((max(list3) + min(list3)) / 2)
print("x0:", list_x0)

# Считаем dx
list_dx = []
list_dx.append(max(list1) - list_x0[0])
list_dx.append(max(list2) - list_x0[1])
list_dx.append(max(list3) - list_x0[2])
print("dx:", list_dx)
print()

# Нормируем X
list_Xn = []
for i in range(len(list1)):
    list_Xn.append([(list1[i] - list_x0[0]) / list_dx[0], (list2[i] - list_x0[1]) / list_dx[1],
                    (list3[i] - list_x0[2]) / list_dx[2]])
print("Нормированные иксы:", list_Xn)
print()

# Считаем средний Y
Y_ser = sum(list_Y) / len(list_Y)
print("Средний Y:", Y_ser)

# Ищем ответ
list_differ = []
for i in list_Y:
    if Y_ser - i >= 0:
        list_differ.append(Y_ser - i)

print("Ответ:", list_X[list_Y.index(Y_ser - min(list_differ))])