from googletrans import Translator
translator = Translator()
file = open('text_4.txt', 'r', encoding = 'utf-8')
list = []

for i in file:
     list += i.split()

for i in range(len(list)):
    if i % 3 == 0:
        result = translator.translate(str(list[i]), src='en', dest='ru')
        list[i] = result.text
    else:
        continue

final = []
for i in range(len(list)):
    if i > 0 and i % 3 == 0:
        final.append('\n')
        final.append(list[i])
    else:
        final.append(list[i])

format = []
for i in range(len(final)):
    if final[i] != '\n':
        format.append(final[i])
        format.append(' ')
    elif final[i] == '\n':
        format.append(final[i])

print(f'{"".join(format)}')
file.seek(0)
file.close()

file = open('text_4_translated.txt', 'w', encoding = 'utf-8')
file.write(f'{"".join(format)}')
file.close()