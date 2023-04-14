# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

def character_count(first_str, second_str):
    count_letters = 0
    count_lettersv2 = []
    letters = []
    for i in range(len(first_str)):
        for j in range(len(second_str)):
            if first_str[i] == second_str[j]:
                count_letters+=1
        if count_letters > 0:
            if first_str[i] not in letters:
                letters.append(first_str[i])
                count_lettersv2.append(count_letters)
            count_letters = 0
    for i in range(len(letters)):
        print(f'{letters[i]} - {count_lettersv2[i]}, ', end="")

first_str = input(str('Введите первую строку: '))
second_str = input(str('Введите вторую строку: '))
if len(first_str) <= len(second_str) : character_count(first_str, second_str)
else : character_count(second_str, first_str)