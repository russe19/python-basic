import re

text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
car = re.findall(r'[АВЕКМНОРСТУХ]\d\d\d[АВЕКМНОРСТУХ]{2}\d\d\d|[АВЕКМНОРСТУХ]\d\d\d[АВЕКМНОРСТУХ]{2}\d\d', text)
taxi = re.findall(r'[АВЕКМНОРСТУХ]{2}\d\d\d\d\d\d|[АВЕКМНОРСТУХ]{2}\d\d\d\d\d', text)
print('Список номеров частных автомобилей: ', car)
print('Список номеров такси: ', taxi)
