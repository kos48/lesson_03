'''Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.'''

def division_func(a, b):
    '''division (a, b)'''
    try:
        result = a / b
    except ZeroDivisionError:
        print('деление на 0!!!')
    else:
        return result

print(division_func(10, 0))
