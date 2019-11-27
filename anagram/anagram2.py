from string import punctuation
from unicodedata import normalize

def cleanstr(str_) -> str:
    str_ = str_.lower()                # Set to lowercase
    str_ = str_.replace(' ','')        # Remove spaces
    str_ = ''.join(
        normalize('NFD', char_)[:1]    # Remove accents
        for char_ in str_
        if char_ not in punctuation    # Remove punctuation
    )
    return str_

def str2dict(str_: str) -> dict:
    str_ = cleanstr(str_)
    dict_ = dict.fromkeys(str_,0)
    for letter in str_:
        dict_[letter] += 1
    return dict_

def is_anagram(str1, str2) -> bool:
    return str2dict(str1) == str2dict(str2)
