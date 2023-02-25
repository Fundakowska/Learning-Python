"""
Implement a function that works the same as the str.split method (without using str.split itself, of course).
"""


def split(data: str, sep=None, maxsplit=-1):
    sentence_list = []

    if sep is not None:
        if maxsplit == -1:
            word = 0
            for i, letter in enumerate(data):
                if data[i:i + len(sep)] == sep:
                    sentence_list.append(data[word:i])
                    word = i + len(sep)
                elif i + 1 == len(data) and len(sep) == 1:
                    sentence_list.append(data[word:i + 1])
            if data[-len(sep):] == sep:
                sentence_list.append('')
        else:
            licznik = 0
            word = 0
            if maxsplit != 0:
                for i, letter in enumerate(data):
                    if licznik < maxsplit:
                        if data[i:i + len(sep)] == sep:
                            sentence_list.append(data[word:i])
                            word = i + len(sep)
                            licznik += 1
                        elif i + 1 == len(data) and len(sep) == 1:
                            sentence_list.append(data[word:i + 1])
                    else:
                        sentence_list.append(data[i + len(sep) - 1:])
                        break
            else:
                sentence_list.append(data)
    else:
        if maxsplit == -1:
            word = ''
            for i, letter in enumerate(data):
                if letter != ' ':
                    word += letter
                if letter == ' ' and word != '':
                    sentence_list.append(word)
                    word = ''
                if i == len(data) - 1 and data[i - 1] == " ":
                    sentence_list.append(word)

        else:
            licznik = 0
            word = ''
            for i, letter in enumerate(data):
                if licznik == maxsplit and word != '':
                    sentence_list.append(data[i - 1:])
                    break
                if letter != ' ':
                    word += letter
                elif letter == ' ' and word != '':
                    sentence_list.append(word)
                    word = ''
                    licznik += 1

    return sentence_list


print(split(''))
