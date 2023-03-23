def is_palindrome_iterative(word):
    if not word:
        return False
    if len(word) == 1:
        return True
    for index, _ in enumerate(word):
        high_index = len(word) - (index + 1)
        if index < high_index and word[index] != word[high_index]:
            return False
    return True
