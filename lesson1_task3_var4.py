'''Сформировать одномерный список целых чисел A, используя генератор случайных чисел (диапазон от 0 до 99).
размер списка n ввести с клавиатуры. В соответствии со своим вариантом написать программу по условию,
представленному в таблице ниже. Вариант 4 Найти значение минимального элемента списка.'''
import random
import numpy as np

A = []
n = int(input(" Enter size of list: "))

for i in range(n):
    new_element = random.randrange(0, 99)
    A.append(new_element)
print(A)
m = min(A)
print("The minimum number in list A is ", m)


