def get_list_number_divisors(number):
    a = []
    for i in range(1, number + 1):
        if number % i == 0:
            a.append(i)
    return a

    ...  # TODO Найдите список делителей числа number


print(get_list_number_divisors(23))
print(get_list_number_divisors(2 ** 16))
