# Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# 1 -> x > 0, y > 0

def range():
    a = int(input("Введите номер четверти: "))

    if a == 1:
        print("Для первой четверти: x от 0 до +∞, y от 0 до +∞") 
    elif a == 2: 
        print("Для второй четверти: x от 0 до -∞, y от 0 до +∞")  
    elif a == 3: 
        print("Для третей четверти: x от 0 до -∞, y от 0 до -∞")
    elif a == 4: 
        print("Для четвёртой четверти: x от 0 до +∞, y от 0 до -∞")

range()