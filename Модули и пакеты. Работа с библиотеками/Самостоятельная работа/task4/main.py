from random import choice


EAGLE = "Орел"
TAILS = "Решка"

coin = [EAGLE, TAILS]  # монета, для которой нужно выбрать случайную сторону
counts = [10, 100, 1000, 100000, 1000000]  # различное количество подбрасываний
list_freq = []  # список, где будем хранить отношение количества выпавших орлов к решке

for count in counts:
    EAGLE_coin = 0
    TAILS_coin = 0

    for _ in range(count):
        count1 = choice(coin)
        if count1 == EAGLE:
            EAGLE_coin += 1
        else:
            TAILS_coin += 1

    res = min(EAGLE_coin, TAILS_coin) / max(EAGLE_coin, TAILS_coin)
    list_freq.append(res)


print(list_freq)
