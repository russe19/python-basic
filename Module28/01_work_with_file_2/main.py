import os


class File:

    def __init__(self, file, type):
        print('Файл открыт')
        self.file = file
        self.type = type
        self.bool = os.path.isfile(file)

    def __enter__(self):
        return self

    def write(self, text):
        try:
            self.f = open(self.file, self.type, encoding='utf-8')
            self.f.write(text)
        except Exception:
            print('Ошибка')

    def read(self):
        if self.bool == False:
            self.f = open(self.file, 'w', encoding='utf-8')
            self.write('')
        else:
            try:
                self.f = open(self.file, self.type, encoding='utf-8')
                reading = self.f.readlines()
                for i in reading:
                    if i.endswith('\n'):
                        print(i[:-1])
                    else:
                        print(i)
            except Exception:
                print('Ошибка')

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.f.close()
            print('Файл закрыт\n')
        finally:
            return True


my_manag_1 = File('file1.txt', 'w')
with my_manag_1 as file:
    file.write('Привет\nТебе')

my_manag_2 = File('file1.txt', 'r')
with my_manag_2 as file:
    file.read()
