import json


FILENAME = "input.json"


def task() -> dict:
    with open(FILENAME, "r") as file:
        jey = json.load(file)
        dict_j = max(jey, key=lambda j: j["score"])
        return dict_j





if __name__ == '__main__':

    print(task())
