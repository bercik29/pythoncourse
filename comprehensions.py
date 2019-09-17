#!/usr/bin/python3

import re

text = 'We met in 2013. She must be now about 27 years old. The film was called Ocean Eleven.'

text_words = []
text_words = re.split(' ', text)

for i in range(len(text_words)):
    pattern = re.compile(r'[A-Z]')
    found = re.findall(pattern, text_words[i])
    if found:
        print(text_words[i]) 