def calculating_math_func(data):
    result = 1
    if data in factorials:
        result = factorials[data]
    else:
        result = max(factorials.values())
        for index in range(max(factorials.keys()) + 1, data + 1):
            result *= index
            factorials[index] = result
    result /= data ** 3
    result = result ** 10
    return result


data = int(input('Введите входное число: '))
factorials = {1: 1}

result = calculating_math_func(data)
print(result)
