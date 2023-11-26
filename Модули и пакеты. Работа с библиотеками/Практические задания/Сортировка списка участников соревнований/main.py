# TODO Напишите функцию sort_participants

def sort_participants(people: list[dict]) -> list:
    list_ = sorted(people, key=lambda p: p["name"])
    return list_

if __name__ == "__main__":
    participants_list = [
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
print(sort_participants(participants_list))
