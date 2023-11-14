# Список словарей со студентами и их оценками
students = [
    {"name": "Маша", "grade": 4},
    {"name": "Петя", "grade": 3},
    {"name": "Саша", "grade": 5},
    {"name": "Кирилл", "grade": 2},
    {"name": "Оля", "grade": 4},
]


for stu in students:
    if stu["grade"] > 3:
        print(f'{stu["name"]}. Оценка: {stu["grade"]}')


