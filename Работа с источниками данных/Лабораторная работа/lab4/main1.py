import json


FILENAME = "input.json"

# TODO решите задачу
def task() -> float:
    with open(FILENAME) as f:
        data = json.load(f)
        sum_score = sum([d["score"] * d["weight"] for d in data])
        return sum_score


a = task()
print(f'{a:.3f}')

