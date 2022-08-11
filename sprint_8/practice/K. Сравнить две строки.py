def compare_string(str_1, str_2):
    new_1 = ''
    new_2 = ''
    for char in str_1:
        if ord(char) % 2 == 0:
            new_1 += char
    for char in str_2:
        if ord(char) % 2 == 0:
            new_2 += char
    if new_1 < new_2:
        return -1
    elif new_1 == new_2:
        return 0
    return 1


def main():
    """Ввести данные, вызвать обработку, напечатать результат."""
    # ввод данных
    with open('input.txt') as file_in:
        # На вход подаются строки a и b по одной в строке.

        first = file_in.readline().strip()
        second = file_in.readline().strip()
        file_in.close()

    print(compare_string(first, second))


if __name__ == '__main__':
    main()
