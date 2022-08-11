RIGHT = 'YES'
WRONG = 'NO'


def check_rized(text, words):
    """_summary_

    Args:
        text (_type_): _description_
        words (_type_): _description_

    Returns:
        _type_: _description_
    """
    return answer


def main():
    """Ввести данные, вызвать обработку, напечатать результат."""
    # ввод данных
    with open('input.txt') as file_in:
        # В первой строке дан текст T, который надо разбить на слова.
        # Длина T не превосходит 105. Текст состоит из строчных букв
        # английского алфавита. 
        # Во второй строке записано число допустимых к использованию
        # слов 1 ≤ n ≤ 100. 
        # В последующих n строках даны сами слова, состоящие из маленьких латинских букв. Длина каждого слова не превосходит 100.
        # Далее в n строках записаны запакованные строки.
        text = file_in.readline().strip()
        num_words = int(file_in.readline())
        words = [None] * num_words
        for idx in range(num_words):
            words[idx] = file_in.readline().strip()

        print(check_rized(text, words))


if __name__ == '__main__':
    main()
