"""Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем сторонами a и b
на квадраты с наибольшей возможной на каждом этапе стороной. Выведите длины ребер получаемых квадратов
 и кол-во полученных квадратов."""

a = int(input("Пожауйста, введите сторону А прямоугольника: "))
b = int(input("Пожауйста, введите сторону В прямоугольника: "))
counter = 0

def big_side(a, b, counter):
    if a == b or b == a:
        print(f" Длина ребра квадрата номер {counter + 1} равна ", a)
        counter += 1
        print(" Всего количество полученных квадратов: ", counter)
        return
    elif a < b:
        print(f" Длина ребра квадрата номер {counter + 1} равна ", a)
        counter += 1
        return big_side(b - a, a, counter)
    else:
        print(f" Длина ребра квадрата номер {counter + 1} равна ", b)
        counter += 1
        return big_side(a - b, b, counter)

big_side(a, b, counter)
