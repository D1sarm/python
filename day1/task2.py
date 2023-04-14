# Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

def distance_between_points():
    ax = float(input('Введите ax: '))
    ay = float(input('Введите ay: '))
    bx = float(input('Введите bx: '))
    by = float(input('Введите by: '))

    print(round(((ax-bx)**2+(ay-by)**2) ** 0.5, 3))

distance_between_points()