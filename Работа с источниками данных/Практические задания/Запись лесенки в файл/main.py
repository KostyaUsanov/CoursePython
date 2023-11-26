INPUT_FILE = "input.txt"


OUTPUT_FILE = "output.txt"


def task():
    with open(OUTPUT_FILE, "w") as f:
        for i in range(1, 11):
            f.write(f'{i * "*"}\n')


# TODO построчно записать лесенку в файл


if __name__ == '__main__':
    # Необходимо для проверки
    task()
    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
