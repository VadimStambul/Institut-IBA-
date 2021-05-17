# Определить, имеется ли среди трёх чисел a, b и c хотя бы одна пара равных между собой чисел.

a = input("Enter integer A for the task: ")
b = input("Enter integer B for the task: ")
c = input("Enter integer C for the task: ")


if a == b == c:
    print('Bingo, all numbers are equal! ')
elif a == b:
    print(" A and B are a pair of equal numbers ")
elif b == c:
    print(" B and C are a pair of equal numbers ")
elif a == c:
    print(" A and C are a pair of equal numbers ")
else:
    print("There are no pair of equal numbers ")
