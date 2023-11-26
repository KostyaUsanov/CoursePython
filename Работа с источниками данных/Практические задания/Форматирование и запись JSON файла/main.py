import json

INPUT_FILE = "input.json"
OUTPUT_FILE = "output.json"


def task() -> None:
    with open(INPUT_FILE, "r", encoding="utf-8") as inp:
        j = json.load(inp)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as o:
        json.dump(j, o, indent=4, ensure_ascii=False)



    ...  # TODO Десериализуйте содержимое файла из переменной INPUT_FILE

    ...  # TODO Сериализуйте содержимое в файл из переменной INPUT_FILE


if __name__ == '__main__':
    # Нужно для проверки задания
    task()

    with open(OUTPUT_FILE, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
