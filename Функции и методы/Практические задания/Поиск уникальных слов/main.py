# TODO реализовать функцию
def get_unique_words(a):
    unique_words = a.split()
    unique_words = list(set(unique_words))
    unique_words.sort()
    return unique_words

print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))
