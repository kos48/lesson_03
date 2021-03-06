'''Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
ранее сумме и после этого завершить программу.'''

sum = 0
x=''

while x != 'exit':
    user_str_number = input('Введите числа разделенные пробелом. Enter - выведет сумму. Q - выведет сумму и выйдет из программы: ')
    user_number = user_str_number.split()
    result = 0

    for i in user_number:
        if i.lower() == 'q':
            x = 'exit'
            break
        try:
            result += int(i)
        except ValueError:
            print('Ввод неверных данных!!!')
    sum += result

    print(f'Сумма всех чисел = {sum}')



