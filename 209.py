import re

def find_numbers(s):
    pattern = r'\b\d{1,3}\b'
    return re.findall(pattern, s)

test = "I have 7 apples,25 mangoes, 123 bananas, and 2025 oranges."
numbers = find_numbers(test)
print("Numbers found:", numbers) 