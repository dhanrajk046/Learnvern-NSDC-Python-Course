import re

def check_string(s):
    return bool(re.fullmatch(r'[A-Za-z0-9]+', s))

test_strings = ["Hello123", "Python", "World2025", "Test@123", "Good_99"]

for s in test_strings:
    print(f"{s}: {check_string(s)}")