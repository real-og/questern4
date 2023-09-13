import unicodedata
import re

def remove_punctuation(s):
    no_punctuation = ''.join([char for char in s if not unicodedata.category(char).startswith('P')])
    no_double_spaces = re.sub(r'\s+', ' ', no_punctuation)
    return no_double_spaces.strip()  


def count_non_matching_digits(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i] and str1[i].isdigit() and str2[i].isdigit():
            count += 1
    return count




