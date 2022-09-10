def is_sqr_exp(num):
    """Вернуть True если num является степенью 4, иначе False.

    Args:
        num (int): проверяемое число

    Returns:
        bool: результат
    """
    if num == 1:
        return True

    # накопитель
    four_val = 4
    # на каждом шаге получаем очередную степень 4
    # если равна - возврат True
    # если больше 10000 - возврат False
    while True:
        if four_val == num:
            return True
        elif four_val > 10000:
            return False
        four_val *= 4


def main():
    number = int(input())

    print(is_sqr_exp(number))


if __name__ == '__main__':
    main()
