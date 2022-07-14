import collections


def can_be_poly(text: str) -> bool:
    counter = collections.Counter(text)
    counter_val = counter.values()
    count_fil = list(filter(lambda x: x % 2, counter_val))
    if len(count_fil) > 1:
        return False
    return True


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
