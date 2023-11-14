# TODO Распечатать таблицу умножения
count = 9
for i in range(2, count + 1):
    for j in range(2, count + 1):
        result = i * j
        end = " " if j != count else ""
        print(f"{result:2}", end=end)
    print()
