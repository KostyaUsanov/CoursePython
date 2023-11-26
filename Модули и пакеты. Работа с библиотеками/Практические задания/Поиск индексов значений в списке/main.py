# TODO написать функцию index
def index(list_: list, value: list) -> list[int]:
    ind = [i for i, val in enumerate(list_) if val == value]
    if not ind:
        raise ValueError("Значение не найдено")
    return ind



if __name__ == '__main__':
    list_items = [1, 2, "3", 1]
    print(index(list_items, 1) == [0, 3])  # True
