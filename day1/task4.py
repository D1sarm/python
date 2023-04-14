# Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

def even_numbers():
    input_number = int(input("Введите целое число N: "))
    numbers = []
    for el in range(1, input_number+1):
        if el%2 == 0:numbers.append(el)
    print(*numbers, sep=", ")
            
even_numbers()
