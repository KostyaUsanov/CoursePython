# TODO Импортируйте Counter из модуля collections
from collections import Counter



if __name__ == '__main__':
    cart_fruits = [
        'Яблоко', 'Банан', 'Апельсин', 'Яблоко', 'Яблоко', 'Яблоко', 'Банан', 'Апельсин', 'Банан', 'Банан',
        'Банан', 'Яблоко', 'Банан', 'Апельсин', 'Банан', 'Апельсин', 'Яблоко', 'Апельсин', 'Банан', 'Банан',
        'Банан', 'Яблоко', 'Апельсин', 'Банан', 'Апельсин', 'Апельсин', 'Апельсин', 'Банан', 'Яблоко', 'Апельсин',
        'Банан', 'Яблоко', 'Банан', 'Банан', 'Банан', 'Апельсин', 'Банан', 'Банан', 'Яблоко', 'Банан', 'Яблоко',
        'Апельсин', 'Яблоко', 'Апельсин', 'Яблоко', 'Апельсин', 'Апельсин', 'Яблоко', 'Апельсин', 'Яблоко'
    ]
grades = Counter(cart_fruits)
print(grades)
    # TODO Подсчитайте фрукты с помощью Counter
