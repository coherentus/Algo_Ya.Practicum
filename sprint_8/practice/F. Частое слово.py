def get_word(words_arr):
    words_dict = dict()
    for word in words_arr:
        count = words_dict.setdefault(word, 0)
        if count == 0:
            words_dict[word] = 1
        else:
            words_dict[word] = count + 1

    max_freq = 0
    max_word = ''

    for word, freq in words_dict.items():
        if freq > max_freq:
            max_freq = freq
            max_word = word
        elif freq == max_freq:
            max_word = min(max_word, word)

    return max_word


def main():
    """Ввести данные, вызвать обработку, напечатать результат."""
    # ввод данных
    with open('input.txt') as file_in:
        # В первой строке дано число n (1 ≤ n ≤ 103) — количество строк.
        # В следующих n строках даны слова

        words_num = int(file_in.readline())
        words = [None] * words_num
        for i in range(words_num):
            words[i] = file_in.readline().strip()
        file_in.close()

    print(get_word(words))


if __name__ == '__main__':
    main()
