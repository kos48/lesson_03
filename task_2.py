'''Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.'''

def user_data_func(name, surname, year_of_birth, current_city = None, email = None, phone = None):
    a = name +' ' + surname + ' ' + str(year_of_birth) + ' ' + str(current_city) + ' ' + str(email) + ' ' + str(phone)
    return a.split()

my_name = 'Konstantin'
my_surname = 'Nikitin'
my_year_of_birth = 1980
my_current_city='Lipezk'
my_email='nikitin.kos.48@yandex.ru'
my_phone = 89001231111

print(user_data_func(name= my_name, surname = my_surname, year_of_birth = my_year_of_birth,  email= my_email, phone = my_phone , current_city=my_current_city))

