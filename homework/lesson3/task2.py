# Задача 2. В списке находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

a = str(input("Введите букву: "))
list = ['абрикос', 'авокадо', 'банан','лимон','айва','ананас','яблоко','брусника', 'бергамот']
for i in range(len(list)):
    list1 = list[i]
    if list1[0] == a:
        print(list1)
