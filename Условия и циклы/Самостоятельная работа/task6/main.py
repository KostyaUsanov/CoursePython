list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_i = max(list_numbers)# TODO Поменяйте местами значения согласно условию

index_max = -1
for idx, value in enumerate(list_numbers):
    if value == max_i:
        index_max = idx

list_numbers[index_max], list_numbers[-1] = list_numbers[-1], list_numbers[index_max]




print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
