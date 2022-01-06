text = 'ewthertyhert'
st = [i for i in range(len(text)) if text[i] == 'h']
new_text = text[:st[0]] + text[st[1]:st[0]:-1] + text[st[1]:]
print('Новый список: ', new_text)