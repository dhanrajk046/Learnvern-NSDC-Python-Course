import re
def match_word_start(text, word):
    pattern = r'^' + re.escape(word)
    if re.match(pattern,text):
        return True
    else:
        return False
print(match_word_start("HelloWorld", "Hello"))   # True
print(match_word_start("HiThere", "There"))      # False
print(match_word_start("Test@123", "Test@"))     # True
print(match_word_start("Learning python","Learn")) #True