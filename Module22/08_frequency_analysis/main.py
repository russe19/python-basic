alphabet = 'abcdefghijklmnopqrstuvwxyz'

letters = dict()
new_let = dict()

file = open('text.txt', 'r')
data = file.read().lower()
file.close()
count_let = 0
for i_elem in data:
    if i_elem in alphabet:
        count_let += 1
        if i_elem in letters:
            letters[i_elem] += 1
        else:
            letters[i_elem] = 1

vals = sorted(letters.values())[::-1]
lets = sorted(letters)

for num in vals:
    for let in lets:
        if letters[let] == num:
            new_let[let] = num
            lets.remove(let)
            break

file_2 = open('analysis.txt', 'w')
for elem in new_let:
    file_2.write(elem + ' ' + str(round((new_let[elem] / count_let), 3)) + '\n')
file_2.close()
