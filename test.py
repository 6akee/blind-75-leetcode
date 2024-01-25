# 1
def replace_str(words: str):
    if not words:
        return words
    words = words[::-1]
    return words


# 2
def replace_str_2(words: str):
    new_words = ""
    for index in range(len(words)-1, -1, -1):
        new_words += words[index]
    return new_words


print(replace_str_2('tabes'))
