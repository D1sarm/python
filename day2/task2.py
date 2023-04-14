#Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

def truth_table():
    for x in range(2):
         for y in range(2):
             for z in range(2):
                 print(f'|{x}|{y}|{z}|', end=' = ')
                 print(not(bool(x) and bool(y)) or bool(z))

truth_table()