# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

def math():
    n = int(input('Введите целое число N: '))
    list = []
    list2 = []
    for el in range(-n, n+1):
        list.append(el)
    for i in range(len(list)):
        list2.append(list[-2+i])
    print(list2)

math()