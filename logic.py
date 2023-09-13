import unicodedata
import re

def remove_punctuation(s):
    
    no_punctuation = ''.join([char for char in s if not unicodedata.category(char).startswith('P')])
    
    no_double_spaces = re.sub(r'\s+', ' ', no_punctuation)
    
    return no_double_spaces.strip()  
