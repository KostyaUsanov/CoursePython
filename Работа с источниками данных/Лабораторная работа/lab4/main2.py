import csv
import json



INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as inp:
        reader = csv.DictReader(inp)
        dict_ = [r for r in reader]

    with open(OUTPUT_FILENAME, "w") as file:
        f = json.dump(dict_, file, indent=4)








if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
