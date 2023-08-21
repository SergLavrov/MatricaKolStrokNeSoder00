# Задача: Дан двумерный массив(двумерная матрица).Определить количество строк,
#         которые не содержат "ноль"

lenX = int(input('Введите количество X: '))
lenY = int(input('Введите количество Y: '))

matrix = [[]] * lenX
for i in range (lenX):
    matrix[i] = [0] * lenY
# print(matrix)

# for i in range (lenX):
#     print(matrix[i])

import random
for i in range(lenX):
    for j in range(lenY):
        matrix[i][j] = random.randint(0, 10)

for i in range(lenX):
    print(matrix[i])

# P.S. Работает по принципу "for item in someList"
# Но в качестве "i" здесь выступает вся строка целиком !!!
# Т.е. если ввести матрицу 3 на 3, то будет всего 3 итерации!
# Если "0" в строке нет то cnt + 1

cnt = 0
for i in matrix:
    if 0 not in i:
        cnt += 1
print(cnt)


