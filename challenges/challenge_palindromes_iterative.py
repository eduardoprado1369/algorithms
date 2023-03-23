def is_palindrome_iterative(word):
    if len(word) == 1:
        return True
    if not word:
        return False
    for index, letter in enumerate(word):
        high_index = len(word) - (index + 1)
        if index < high_index:
            if letter != word[high_index]:
                return False
    return True
