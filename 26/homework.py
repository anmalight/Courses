'''
1) Задача, написать класс, который будет работать с контекстным менеджером, чтобы можно профилировать участок кода.
2) Написать класс, который будет читать .csv любых размеров, и будет отдавать ответ построчно аля генератор
'''


# 1
import time
class Profiler():

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        duration = (time.time() - self.start) * 1000 # милисекунд вроде бы
        message = f"Duration : {duration}"
        print(message)


work_time =  Profiler()
with work_time:
    print(1000**1000)


# 2
class ReadCSV:

    def read_str_by_str(self, file):
        with open(file) as f:
            for line in f:
                line.split('\n')
                print(line)


d = ReadCSV()
d.read_str_by_str('convertcsv.csv')
