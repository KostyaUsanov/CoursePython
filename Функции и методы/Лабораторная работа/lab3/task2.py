# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, arg=","):
    participants_first_group1 = participants_first_group.split("|")
    participants_second_group2 = participants_second_group.split("|")
    common_group = list(set(participants_first_group1).intersection(participants_second_group2))
    common_group.sort()
    return common_group
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"



# TODO Провеьте работу функции с разделителем отличным от запятой
print(f"Общие участники: {find_common_participants(participants_first_group, participants_second_group)}")
