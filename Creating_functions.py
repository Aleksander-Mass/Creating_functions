# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'

# Используем lambda-функцию в map
result = list(map(lambda x, y: x == y, first, second))
print(result) # => [False, True, True, False, False, False, False, False, True, False, False, False, False, False]

# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a') as f:
            for item in data_set:
                f.write(str(item) + '\n')
    return write_everything

# Пример использования
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Этот код создает файл example.txt, в который будут добавлены данные:
'''
Это строчка
['А', 'это', 'уже', 'число', 5, 'в', 'списке']
'''

# Метод __call__:
from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

# Пример использования
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())  # Случайный результат
print(first_ball())  # Случайный результат
print(first_ball())  # Случайный результат