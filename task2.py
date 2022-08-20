'''
2. На языке Python (2.7) реализовать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.
'''
# С вашего позволения напишу на Python 3.9.5 чтобы не тратить время на установку и настройку Python 2.7


class CycleBufer:
    # при инициализации будем указывать количество ячеек для хранения информации
    def __init__(self, quanity_storage):
        # хранить данные будем в виде списка
        self.storage = [None for _ in range(0, quanity_storage)]
        self.count = 0

    # метод добавления данных в буфер
    def add_data(self, data):
        if self.count < len(self.storage):
            self.storage[self.count] = data
            self.count += 1
        else:
            self.count = 0
            self.storage[self.count] = data
            self.count += 1

    # метод удаления данных из буфера
    def del_data(self):
        if self.count < len(self.storage):
            self.storage[self.count] = None
            self.count += 1
        else:
            self.count = 0
            self.storage[self.count] = None
            self.count += 1

    def __str__(self):
        return str(self.storage)


class CycleBufer2:
    def __init__(self, quanity_storage):
        self.storage = [None for _ in range(0, quanity_storage)]

    # метод добавления данных в буфер
    def add_data(self, data):
        self.storage.append(data)
        self.storage.pop(0)

    # метод удаления данных из буфера
    def del_data(self):
        self.storage.append(None)
        self.storage.pop(0)

    def __str__(self):
        return str(self.storage)


'''
Оба класса основаны на списках.

В первом методы реализованы с помощью дополнительной переменной-счётчика
плюс: добавление и и удаление происходит поиндексно (ускоряет работу)
минус: дополнительная переменная

Во втором используются встроенные методы работы со списками
плюс: меньше переменных и операций над ними, меньше кода
минус: пересчёт индексов очень ресурсозатратно

'''

if __name__ == '__main__':
    bufer_1 = CycleBufer(5)
    print(bufer_1)
    bufer_1.add_data(1)
    bufer_1.add_data('2')
    bufer_1.add_data(3)
    bufer_1.add_data('4')
    bufer_1.add_data(5)
    print(bufer_1)
    bufer_1.add_data(6)
    bufer_1.add_data(7)
    print(bufer_1)
    bufer_1.del_data()
    print(bufer_1)
    bufer_1.del_data()
    print(bufer_1)
    print('='*50)
    bufer_2 = CycleBufer2(5)
    print(bufer_2)
    bufer_2.add_data(1)
    bufer_2.add_data('2')
    bufer_2.add_data(3)
    bufer_2.add_data('4')
    bufer_2.add_data(5)
    print(bufer_2)
    bufer_2.add_data(6)
    bufer_2.add_data(7)
    print(bufer_2)
    bufer_2.del_data()
    print(bufer_2)
    bufer_2.del_data()
    print(bufer_2)
