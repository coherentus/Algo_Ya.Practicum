def get_reverse_line(words_arr):
    left = 0
    right = len(words_arr) - 1
    while left < right:
        words_arr[left], words_arr[right] = (
            words_arr[right], words_arr[left]
        )


def main():
    """Ввести данные, вызвать обработку, напечатать результат."""
    # ввод данных
    with open('input.txt') as file_in:
        # На ввод подаётся строка, состоящая из слов, разделённых пробелами
        # (один пробел между соседними словами). Всего слов не более 1000,
        # длина каждого из них —– от 1 до 100 символов.
        # Слова состоят из строчных букв английского алфавита.
        words = file_in.readline().split()
        #get_reverse_line(words)
        for idx in range(len(words) - 1, -1, -1):
            print(words[idx], end=' ')

if __name__ == '__main__':
    main()
