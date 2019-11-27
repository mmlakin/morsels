from collections import Counter
from unicodedata import normalize

def clean_word(word):
    word = word.lower()
    word = word.replace(' ','')
    word = ''.join(
        normalize('NFKD', char)[:1]
        for char in word
        if char.isalpha()
    )
    return word

def is_anagram(word1, word2):
    return Counter(clean_word(word1)) == Counter(clean_word(word2))
