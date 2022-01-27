# https://contest.yandex.ru/contest/22450/run-report/64566737/
# Задача: Есть набор символов ".123456789". Из них произвольным
# образом формируется матрица 4х4. Дано число k.
# Для девяти циклов с номерами от 1 до 9 необходимо определить
# в скольких циклах цифра этого номера содержится в матрице
# в количестве не более k.
#
# Вариант решения.
# 1. Создать нулевой ответ.
# 2. Удалить из матрицы символы точки.
# 3. Создать вспомогательный массив - математич. множество из эл-в матрицы.
# 4. Для каждого из эл-в этого множества подсчитывать кол-во его вхождений
# в матрицу. Если значение не превосходит k, добавить 1 к результату.
from typing import Set


def score_count(key_matrix: str, fingers: int) -> int:
    fingers_all: int = fingers * 2
    result: int = 0
    key_matrix_num: str = key_matrix.replace('.', '')
    uniq_buttons: Set[str] = set(key_matrix_num)

    for key in uniq_buttons:
        if key_matrix_num.count(key) <= fingers_all:
            result += 1
    return result


def main():
    fingers: int = int(input())
    matrix: str = ''
    matrix = ''.join(input() for _ in range(4))
    score: int = score_count(matrix, fingers)
    print(score)


if __name__ == '__main__':
    main()
