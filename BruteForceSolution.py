from itertools import combinations

binary_words = [] # binary words here

def is_uniquely_decodable(code):
    for i, word1 in enumerate(code):
        for j, word2 in enumerate(code):
            if i != j and (word1.startswith(word2) or word2.startswith(word1)):
                return False
    return True

def is_not_prefix_free_after_reversal(code):
    reversed_code = [word[::-1] for word in code]
    for i, word1 in enumerate(reversed_code):
        for j, word2 in enumerate(reversed_code):
            if i != j and (word1.startswith(word2) or word2.startswith(word1)):
                return False
    return True

def check_code(code):
    if is_uniquely_decodable(code) and not is_not_prefix_free_after_reversal(code):
        return True
    return False

if check_code(binary_words):
    print("All conditions")
else:
    print("Does not meet all conditions.")
