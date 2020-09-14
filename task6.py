def int_func(a):
    sentence_final = []
    sentence_sum = []
    dict = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}

    sentence_in_list = a.split()
    for i in range(len(sentence_in_list)):
        word = sentence_in_list[i]
        letter = list(word)
        for l in range(len(letter)):
            if letter[0] in dict:
                letter[0] = dict[letter[0]]

        word_final = ''
        word_final = word_final.join(letter)

        sentence_sum.append(word_final)

    sentence_final = ' '
    sentence_final = sentence_final.join(sentence_sum)

        #print(''.join(sentence_final))
    return f'{sentence_final}'

print(int_func('capitalisation of all first letters of all words of the sentence'))