number = 2342354235235

# TODO c помощью list comprehension получить список цифр числа

digits_list = [int(d) for d in str(number)]  # приводим каждый символ к числу


print(sum(digits_list))  # TODO найти сумму цифр числа
# print(sum(filter(lambda x: not x % 2, digits_list)))
print(sum(num for num in digits_list if not num % 2))# TODO найти сумму всех четных чисел
print(len(digits_list))  # TODO найти количество цифр
print(min(digits_list))  # TODO найти минимальную цифру
print(digits_list[0] - digits_list[-1])  # TODO найти разность между первой и последней цифрой
