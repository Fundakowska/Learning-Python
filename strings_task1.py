"""
Implement a function get_longest_word(s: str) -> str which returns the longest word in the given string.
The word can contain any symbols except whitespaces (' ', '\n', '\t' and so on).
If there are multiple longest words in the string with the same length return the word that occurs first.
"""

def get_longest_word(s: str) -> str:
    word = s.replace('-', " ").replace('.', " ").replace('\t', " ").replace('\n', " ")
    word = word.split(" ")
    sortedwords = sorted(word, key=len)[::-1]
    last_word = ""
    for i, word in enumerate(sortedwords):
        if len(sortedwords[i]) == (len(sortedwords[i+1])):
            continue
        else:
            last_word = word
            break
    return last_word

print(get_longest_word('Python is simple and effective!'))