# TODO Напишите функцию calculate_average_age
def calculate_average_age(students: list[dict]) -> list[int]:
    all_age = [student["age"] for student in students]
    return sum(all_age)/len(all_age)

# TODO Напишите функцию filter_students_by_age
def filter_students_by_age(students: list[dict], middle_age):
    all_ages = [student for student in students if student["age"] < middle_age]
    return all_ages
    # print(students["name"])

if __name__ == '__main__':
    # Пример списка учеников
    students_list = [
        {
            "name": "Саша",
            "age": 27,
        },
        {
            "name": "Кирилл",
            "age": 52,
        },
        {
            "name": "Маша",
            "age": 14,
        },
        {
            "name": "Петя",
            "age": 36,
        },
        {
            "name": "Оля",
            "age": 43,
        },
    ]

    # Вычисление среднего возраста
    # TODO Вычислите средний возраст учеников
    middle_age = calculate_average_age(students_list)
    print("Средний возраст учеников:", middle_age)

    # Фильтрация учеников по возрасту
    # TODO Офильтруйте учеников
    list_filter_stu = filter_students_by_age(students_list, middle_age)
    print("Список учеников с возрастом меньше среднего:")
    for current_student in list_filter_stu:
        print(current_student['name'])
