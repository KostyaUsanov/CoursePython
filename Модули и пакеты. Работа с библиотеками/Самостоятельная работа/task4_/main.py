
from typing import Any


def remove(list_: list, val: Any) -> list:
    res = None
    for i, cur_val in enumerate(list_):
        if cur_val == val:
            res = i

    if res is None:
        raise ValueError("Этого элемента нет в списке")
    else:
        return list_[:res] + list_[res + 1:]





print(remove([0, 1, 2, 0, 1, 2], 0))  # [0, 1, 2, 1, 2]
print(remove([0, 1, 2], 0))  # [1, 2]
print(remove([0, 1, 2, 3, 4], 4))  # [0, 1, 2, 3]
