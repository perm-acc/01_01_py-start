sentence = input('Введите слова через пробел: ')
words_list = list(sentence.split())
i = 0
while i < len(words_list):
        print(f'{i+1}. {str(words_list[i])[0:10]}')
        i+=1