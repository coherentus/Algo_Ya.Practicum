def factor(number):
    """Найти и вернуть разложение на множители входного числа.

    Args:
        number (int): входное число.

    Returns:
        list of int: найденные множители.

    Минимальный множитель 2, максимальный - корень кв из числа. В этом
    диапазоне в цикле проводится проверка на делимость числа на текущий
    делитель. Делитель проверяется до тех пор, пока число делится.
    Найденые множители добавляются в массив. После каждого удачного деления
    частное становится проверяемым для следующего шага.
    """
    result = []
    d = 2
    while d * d <= number:
        if number % d == 0:
            result.append(d)
            number //= d
        else:
            d += 1
    if number > 1:
        result.append(number)
    return result


def main():
    num = int(input())
    result = factor(num)
    print(*result)
    # print(*sorted(result))


if __name__ == '__main__':
    main()
