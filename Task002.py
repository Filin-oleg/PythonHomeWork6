# Предложить улучшения кода для уже решённых задач.
# Семинар 3. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.


import random


def input_number(text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{text}"))
            is_OK = True
        except ValueError:
            print("Это не натуральное число! Повторите ввод")
    return number


def fill_list(n: int, border_min: int, border_max: int) -> list:
    if border_min < border_max:
        min, max = border_min, border_max
    else:
        min, max = border_max, border_min
    list = [random.randint(min, max)]
    for i in range(1, n):
        list.append(random.randint(min, max))
        i += 1
    return list


n = input_number(" Введите количество элементов списка: ")
border_min = input_number("Введите нижнюю границу значений элементов списка: ")
border_max = input_number(" Введите верхнюю границу значений элементов списка: ")
list = fill_list(n, border_min, border_max)
sum_odd = sum(list[item] for item in range(1, len(list), 2))
odd_elements = str([list[item] for item in range(1, len(list), 2)]).strip('[]')
print(f"Сумма элементов списка {list}, стоящих на нечётной позиции \n{odd_elements} = {sum_odd};")
