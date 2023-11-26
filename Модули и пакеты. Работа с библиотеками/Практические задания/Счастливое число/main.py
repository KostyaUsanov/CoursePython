def is_lucky_number(num: int) -> bool:
    if len(str(num)) != 6:
        raise ValueError("Число не шестизначное")

    if num < 0:   # TODO проверить что число шестизначное и положительное
        raise ValueError("Число не является положительным")

    lucky_number = [int(n) for n in str(num)]
    return sum(lucky_number[:3]) == sum(lucky_number[3:])

     # TODO проверить счастливое число или нет


print(is_lucky_number(123321))
print(is_lucky_number(111111))
print(is_lucky_number(123456))
print(is_lucky_number(456243))
