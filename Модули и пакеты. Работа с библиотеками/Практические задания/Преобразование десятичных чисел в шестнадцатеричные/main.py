# TODO Напишите функцию decimal_to_hex
def decimal_to_hex() -> dict[int, str]:


    return {decimal: hex(decimal) for decimal in range(16)}


if __name__ == '__main__':
    ...  # TODO Распечатайте словарь с десятичными и шестнадцатеричными числами

dict_decimal = decimal_to_hex()
print(dict_decimal)

