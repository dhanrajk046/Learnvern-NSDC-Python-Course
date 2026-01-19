import re

def check_only_letters(s):
    pattern = r'^[A-Za-z]+$'
    return bool(re.match(pattern, s))

test_strings = ["Hello", "WORLD", "python", "Python3", "Test@"]

for text in test_strings:
    print(f"{text}: {check_only_letters(text)}")