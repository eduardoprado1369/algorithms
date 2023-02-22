def is_anagram(first_string: str, second_string: str):
    if not first_string and not second_string:
        return (first_string, second_string, False)

    sorted_first_string_list = merge_sort(first_string)
    sorted_second_string_list = merge_sort(second_string)

    sorted_first_string = "".join(sorted_first_string_list)
    sorted_second_string = "".join(sorted_second_string_list)

    if sorted_first_string.lower() == sorted_second_string.lower():
        return (sorted_first_string.lower(), sorted_second_string.lower(),
                True)
    return (sorted_first_string.lower(), sorted_second_string.lower(), False)


# funções merge_sort e merge baseadas nas funções da aula 3 da seção 4
def merge_sort(word: str):
    if len(word) <= 1 or not word:
        return word

    word_list = [letter for letter in word]

    mid = len(word_list) // 2

    left = merge_sort(word_list[:mid])
    right = merge_sort(word_list[mid:])

    return merge(left, right)


def merge(left: list, right: list):
    result = list()
    while len(left) > 0 and len(right) > 0:
        if left[0].lower() < right[0].lower():
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) == 0:
        result += right
    else:
        result += left
    return result
