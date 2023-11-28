"""
Прототип консольного приложения для игры в виселицу
"""

import random
import json
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def choose_word(word_len: int) -> str:
    """
    Функция выдаёт случайное слово по заданной длине
    :param word_len: длина слова
    :return: слово
    """
    with open("database.json", encoding="utf-8") as f:
        words = json.load(f)
    filtered_words = [word for word in words if len(word) == word_len]
    return random.choice(filtered_words)


def display_word(word: str, view_letter: list) -> str:
    """
    Выводит слово на экран с открытыми буквами, если они угаданы
    :param word: искомое слово
    :param view_letter: список букв, что были произнесены
    :return: строковое представление
    """
    display = ""
    for letter in word:
        if letter in view_letter:
            display += letter
        else:
            display += "_"
    return display


def check_player_letter(view_letter):
    while True:
        player_letter = input("Введи букву: ").lower()

        if len(player_letter) != 1 or not player_letter.isalpha():
            print("Пожалуйста, введите только одну букву!")
            cls()
            continue

        if ord("A") <= ord(player_letter) <= ord("z"):
            print("Пожалуйста, введите кириллическую букву!")
            cls()
            continue

        if player_letter in view_letter:
            print("Вы уже вводили эту букву. Попробуйте другую!")
            cls()
            continue

        return player_letter


def game():
    print("Добро пожаловать в игру Виселица!")

    word_length = int(input("Введи длину слова для угадывания: "))  # TODO ограничить длину слова
    max_attempts = int(input("Введи максимальное число неудачных попыток: "))

    secret_word = choose_word(word_length).lower()
    view_letter = []
    attempts = 0

    while attempts < max_attempts:
        current_display = display_word(secret_word, view_letter)
        print(f"Текущее состояние слова: {current_display}")

        player_letter = check_player_letter(view_letter)

        view_letter.append(player_letter)

        if set(view_letter) >= set(secret_word):
            print(f"Вы выиграли! Угадали слово: {secret_word}")
            return True

        if player_letter not in secret_word:
            attempts += 1
            print(f"Неверная буква! Осталось попыток: {max_attempts - attempts}")

    print(f"Игра окончена. Вы не угадали слово. Слово было {repr(secret_word)}")
    return False


if __name__ == "__main__":
    # random.seed(0)
    # word = choose_word(5)
    # print(word)
    # print(display_word(word, ["е"]))
    game()
