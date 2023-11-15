# TODO  Напишите функцию count_letters
def count_letters(text):
    main_str1 = "".join(text.lower().split())
    main_str_res = {}

    for char in main_str1:
        if char.isalpha():
            if char in main_str_res:
                main_str_res[char] += 1
            else:
                main_str_res[char] = 1

    return main_str_res


 # def calculate_frequency(letter):
 #    count_letters(text)
 #    new_dict_ = {}
 #    main_str_len = len(count_letters())
# TODO Напишите функцию calculate_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
# main_str1 = {}
# main_str1 = "".join(main_str.lower().split())
# # if main_str1.isalpha():
# #     print(main_str)
# str_ = 0
# for st in main_str:
#     str_ += 1
# main_str_len = len(main_str1)
# print(main_str_len)
# print(main_str1)

# TODO Распечатайте в столбик букву и её частоту в тексте

res = count_letters(main_str)

for key, value in res.items():
    print(key, value)