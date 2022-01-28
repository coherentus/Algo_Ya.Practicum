# https://contest.yandex.ru/contest/22450/run-report/64592814/
# Задача: Есть набор символов ".123456789". Из них произвольным
# образом формируется матрица 4х4. Дано число k.
# Для девяти циклов с номерами от 1 до 9 необходимо определить
# в скольких циклах цифра этого номера содержится в матрице
# в количестве не более k.
#
# Вариант решения.
# За один проход по матрице подсчитать все вхождения каждого символа,
# затем подсчитать те символы, вхождение которых не больше k.
#
#  Смысл алгоритма:
#
# 1. Создать нулевой ответ.
# 2. Создать пуcтой словарь.
# Ключ - символ, значение - счётчик вхождений.
# 3. В итерации по матрице: точки пропускать, проверить ключ в словаре.
# Если нет - создать со значением 1.
# Если есть - увеличить счётчик на 1.
#
# 4. В итерации по словарю сравнить значение (счётчик) с k.
# Если счётчик <= k то увеличить на 1 результат.

def score_count(key_matrix: str, fingers: int) -> int:
    fingers_all: int = fingers * 2
    result: int = 0
    temp_counts: dict = dict()

    for char in key_matrix:
        if char == '.':
            continue

        if char in temp_counts:
            temp_counts[char] += 1
        else:
            temp_counts[char] = 1

    for value in temp_counts.values():
        if value <= fingers_all:
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
