'''
3. На языке Python реализовать функцию, которая быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить почему вы считаете, что функция соответствует заданным критериям.
'''


def my_sort(numbers):
    while True:
        flag = False
        for i in range(0, len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                flag = True
        if flag == False:
            break


'''
Заранее извиняюсь за это решение. Понимаю, что алгоритм очень долгий и примитивный.
Зато написал я его сам, и он работает.
Мог бы скопировать из интернета достойное решение, но это не соответствовало бы моим реальным навыкам.
Но если мне приходится копировать чужой код, и разбираться как он работает, я это делаю.
'''


if __name__ == '__main__':
    from random import randint

    numbers = [randint(1, 100) for _ in range(100)]
    print(numbers)
    print('='*50)
    my_sort(numbers)
    print('='*50)
    print(numbers)