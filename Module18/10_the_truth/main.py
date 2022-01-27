text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

m = 0
s = ''
for i in range(len(text)):
    if text[i] in alphabet:
        m = alphabet.index(text[i])
        s += alphabet[(m - 1) % 52]
        m = 0
    else:
        s += text[i]

s_list = s.split()
shift = 3
new_list = []
for word in s_list:
    if '/' in word:
        shift += 1
    for i in range(shift):
        word = word[-1::] + word[:-1:]
    new_list.append(word)
new_text = ' '.join(new_list)
new = ''
for i in new_text:
    if i == '(':
        i = "'"
    elif i == '+':
        i = '"'
    elif i == '/':
        i = ''
    new += i
print(new)

# TODO
#  Каждое слово зашифровано отдельно шифром Цезаря.
#  Судя по первому  слову можно увидеть, что имеет место циклический сдвиг влево на три символа
#  После слова с символом "/" циклический сдвиг увеличивается на один и очередное слово содержит заглавную букву.
#  Есть несколько способов, один из них несколько списков.
#  1) приводить буквы в индексы алфавита
#  2) использовать их для смещения
#  3) после   лучше удалить лишнее, вернее заменить - '(' и '+' на одинарные "'" и двойные кавычки '"'
#  Примерно такие слова получатся в списке после данных действий
#  text = ['utifulbea', 'terbet', 'si' ...
#  Останется расшифровать пройтись по нему  циклами, сдвигая буквы соответственно индексу предложения
#  .
#  Еще один способ - это 25 итераций цикла с дешифровкой слов, но также нужно учесть замену символов
#  Примерный алгоритм:
#   расшифровываем слово
#   Далее с помощью цикла проверяем лишние символы для замены.
#   К примеру заменяем символы '(' и '+' на одинарные "'" и двойные кавычки '"
#   Берем текущий символ находим его в алфавите .find , если есть символы для замены заменяем и добавляем к расшифровке
#   .
#   В другом случае нужно рассчитать индекс буквы
#   (значение буквы в алфавите + смещение) % 26
#   И также добавляем к расшифровке, но уже обращаясь к алфавиту по рассчитанному индексу
#   примерно так: алфавит[(значение буквы в алфавите + смещение) % 26]
#   .
#   В целом цикл по алфавит и замене вам очень поможет, когда нужно будет расшифровать к примеру - 'tju('
#   В нем зашифровано "it's"
