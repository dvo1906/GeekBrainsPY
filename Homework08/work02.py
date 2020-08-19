# Задание-2:
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
# нуля в качестве делителя программа должна корректно обработать эту ситуацию и
# не завершиться с ошибкой.


class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return divider / denominator
        except ZeroDivisionError:
            return f"Деление на ноль недопустимо"


Stop = False
while not Stop:
    print(DivisionByNull.divide_by_null(float(input('Введите делимое и нажмите Enter - ')),
                                        float(input('Введите делитель и нажмите Enter - '))))
    y_or_n = input(f'Попробовать еще раз? Y/N ')
    if y_or_n == 'Y' or y_or_n == 'y':
        Stop = False
    elif y_or_n == 'N' or y_or_n == 'n':
        Stop = True
    else:
        Stop = True
