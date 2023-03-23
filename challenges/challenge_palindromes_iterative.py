def is_palindrome_iterative(word):
    # print(word)
    if len(word) == 1:
        return True
    if not word:
        return False
    for index in range(len(word)):
        high_index = len(word) - (index + 1)
        if index < high_index:
            # print(index)
            # print(word[index])
            # print(high_index)
            if word[index] != word[high_index]:
                return False
    return True