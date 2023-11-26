# # TODO Напишите функцию find_common_participants
# def find_common_participants(first_group, second_group, arg=","):
#     participants_first_group1 = first_group.split(arg)
#     participants_second_group2 = second_group.split(arg)
#     common_group = list(set(participants_first_group1).intersection(participants_second_group2))
#     common_group.sort()
#
#     return common_group
#
#
# participants_first_group = "Иванов|Петров|Сидоров"
# participants_second_group = "Петров|Сидоров|Смирнов"
#
# find_common_participants1 = find_common_participants(participants_first_group, participants_second_group)
# print("Общие участники", find_common_participants1)


def find_common_participants(participants1, participants2, separator=','):
    participants_list1 = participants1.split(separator)
    participants_list2 = participants2.split(separator)

    common_participants = list(set(participants_list1).intersection(participants_list2))
    common_participants.sort()

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group, separator="|")
print("Общие участники:", participants)
