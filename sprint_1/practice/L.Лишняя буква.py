def extra_letter(first, second: str):
    """Найти и вернуть букву во второй строке, отсутствующую в первой.

    Args:
        first (str): исходная строка
        second (str): перемешанная строка с лишней буквой

    Returns:
        str: добавленная буква

    Перебирая символы второй строки проверить их количество в первой
    и второй строках, если кол-во различно, то это искомый символ.
    """
    for letter in second:
        if second.count(letter) != first.count(letter):
            return letter
    return


def main():
    string_1: str = input()
    string_2: str = input()
    answer: str = extra_letter(string_1, string_2)
    print(answer)


if __name__ == '__main__':
    main()
