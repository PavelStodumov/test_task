'''1. На языке Python реализовать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций.

Python example:

def isEven(value):return value%2==0'''

# суть алгоритма основана на изменении типов


def is_even(value):
    try:
        # после деления на 2 анализируем часть значения после точки
        # и если в ней есть что-то кроме "0", возвращаем False
        return not bool(int(str(int(value) / 2).split('.')[1]))
    except ValueError:
        print(f'Некорректное значение {value}')


'''
Плюс моего решения в работе со строковыми значениями и в обработке исключений
Минусы конечно в производительности из за количества вычислений
'''


if __name__ == '__main__':
    print(is_even(2))
    print(is_even(3))
    print(is_even('2'))
    print(is_even(0))
    print(is_even('2d'))
