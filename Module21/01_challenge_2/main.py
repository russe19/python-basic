def subsequence(number, n):
    if n < number:
        n += 1
        print(n)
        return subsequence(number, n)
    else:
        return 1


number = int(input('Введите число: '))
n = 0
subsequence(number, n)
