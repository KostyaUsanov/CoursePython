# TODO реализовать функцию
def remove_whitespace(a):
    words = a.split(" ")
    words_list = []
    for word in words:
        if word:
            words_list.append(word)
            a = " ".join(words_list)
    return a



str_with_space = """123.    test bks
print   test11"""  # исходная строка

print(remove_whitespace(str_with_space))
