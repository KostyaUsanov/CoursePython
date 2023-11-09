def exists_student_by_lastname(students, lastname):
    for student in students:
        if student['фамилия'] == lastname:
            return True
    return False

    ...  # TODO Напишите проверку студента с заданной фамилией


students_list = [
    {'имя': 'Иван', 'фамилия': 'Иванов'},
    {'имя': 'Петр', 'фамилия': 'Петров'},
    {'имя': 'Анна', 'фамилия': 'Иванова'},
    {'имя': 'Елена', 'фамилия': 'Сидорова'},
]

for find_lastname in ['Иванов', 'Пупкин', 'Дупкин', 'Сидорова']:
    is_exists_lastname = exists_student_by_lastname(students_list, find_lastname)
    print(f"Есть ли в базе студент с фамилией {find_lastname}? {is_exists_lastname}")
