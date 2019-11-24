'''
1) Задача, написать класс, который будет работать с контекстным менеджером, чтобы можно профилировать участок кода.
2) Написать класс, который будет читать .csv любых размеров, и будет отдавать ответ построчно аля генератор
'''

# 1
import time


class Profiler(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        duration = (time.time() - self.start)
        message = f"{self.name} : {duration}"
        print(message)


def func_11(arg):
    return arg ** arg


with Profiler(func_11(12)):
    pass


# 2
class ReadCSV:

    def read_str_by_str(self, file):
        with open(file) as f:
            for line in f:
                print(line)


d = ReadCSV()
d.read_str_by_str('convertcsv.csv')
