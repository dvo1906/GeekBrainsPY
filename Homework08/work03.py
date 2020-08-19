# Задание-3:
# Создайте собственный класс-исключение, который должен проверять содержимое списка
# на отсутствие элементов типа строка и булево. Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.


class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                return f'Текущий список - {self.my_list} \n '
            except ValueError:
                return False


try_except = Error(1)
Stop = False
while not Stop:
    checkList = try_except.my_input()
    if not checkList:
        print(f"Недопустимое значение - строка или булево")
        y_or_n = input(f'Продолжить ввод? Y/N ')
        if y_or_n == 'Y' or y_or_n == 'y':
            Stop = False
        elif y_or_n == 'N' or y_or_n == 'n':
            Stop = True
        else:
            Stop = True
    else:
        print(checkList)
