'''Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.'''

def sum_max(a, b, c):
    z = min(a, b, c)
    if z == a:
        result = b + c
    elif z == b:
        result = a + c
    else:
        a + b
    return result

print(sum_max(8,3,3))

#3
