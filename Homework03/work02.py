# Задание - 2:
# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой

def my_func(name, surname, byear, city, email, phone):
    print(name, surname, byear, city, email, phone)


my_func(name='dmitrii', surname='dvo', byear=1982, city='Krs', email='mail', phone='0000')
