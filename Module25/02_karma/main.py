import random


def one_day():
    if random.randint(1, 10) == 1:
        log = (random.choice(['KillError', 'DrunkError', 'CarCrashError',
                              'GluttonyError', 'DepressionError']) + '\n')
        file.write(log)
    return random.randint(1, 7)


karma = 0
with open('karma.log', 'w') as file:
    while karma < 500:
        karma += one_day()
print('Просветление достигнуто!')
