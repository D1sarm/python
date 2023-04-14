# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial():
    n = int(input("Введите целое число N: "))
    j = 1
    numbers = []
    numbers2 = []
    for i in range(1, n+1):
        j = i*j
        numbers.append(j)
        numbers2.insert(j,i)
        print(*numbers2, sep="*", end=' \n')
    print(numbers)
    
factorial()