""" Решение однострочным кодом """
first = [i for i in range(1001)]
print('first: ', first)

second = list(map(lambda x: x, range(1001)))
print('second: ', second)

""" Решение другим способом """
i = 0
third = []
while i <= 1000:
    third.append(i)
    i += 1
print('third: ', third)
