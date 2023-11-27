import json


FILENAME = "input.json"


def task() -> int:
    with open(FILENAME, "r") as file:
        jey = json.load(file)
        dict_j = [j["contains_improvement_appeals"] for j in jey]
        return sum(dict_j)



    ...  # TODO Десериализуйте содержимое JSON файла

    ...  # TODO Просуммируйте все значения по ключу contains_improvement_appeals


if __name__ == '__main__':
    print(task())
