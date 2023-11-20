# TODO Напишите функцию calculate_average_age для расчета среднего возраста студентов
def calculate_average_age(b):
    c = b.values()
    a = sum(c) / len(c)
    return a

students_dict = {
    'Саша': 27,
    'Кирилл': 52, 
    'Маша': 14, 
    'Петя': 36, 
    'Оля': 43, 
}

d = calculate_average_age(students_dict)

print(f"Средний возраст студентов: {d}")  # TODO Распечатайте средний возраст студентов
