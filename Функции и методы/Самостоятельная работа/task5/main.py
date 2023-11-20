def get_sentences_list(a):
    list_ = []
    for li in a.split("."):
        if li:
            list_.append(li.strip())
    return list_



print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))
