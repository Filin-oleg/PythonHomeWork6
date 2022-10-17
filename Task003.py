# Предложить улучшения кода для уже решённых задач.
# Семинар 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.


from random import randint
import itertools


def input_number(text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{text}"))
            is_OK = True
        except ValueError:
            print("Это не натуральное число! Повторите ввод")
    return number


def fill_coefficients(k):
    coeff = [randint(0, 100) for i in range(k + 1)]
    while coeff[0] == 0:
        coeff[0] = randint(0, 100)
    return coeff


def get_polynomial(k, coeff):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(
        coeff, var, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x', ' x')


k = input_number("Задайте натуральную степень многочлена k: ")
coeff_polynom = fill_coefficients(k)
polynom = get_polynomial(k, coeff_polynom)
with open('Polynominal.txt', 'w') as data:
    data.write(polynom)
print(f"Многочлен заданной Вами степени {k} = {polynom} и записан в файл [Polynominal.txt] ")
