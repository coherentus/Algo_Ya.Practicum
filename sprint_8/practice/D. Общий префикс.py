def get_prefix(strs):
    max_prefix = 0
    for col in range(len(strs[0])):
        char = strs[0][col]
        for row in range(1, len(strs)):
            if strs[row][col] != char:
                return max_prefix
        max_prefix += 1
    return max_prefix


def main():
    """Ввести данные, вызвать обработку, напечатать результат."""
    # ввод данных
    with open('input.txt') as file_in:
        # В первой строке дано число n (1 ≤ n ≤ 105).
        # Затем по одной на строке даны n строк.

        strs_num = int(file_in.readline())
        strs = [None] * strs_num
        for i in range(strs_num):
            strs[i] = file_in.readline().strip()
        file_in.close()

    print(get_prefix(strs))


if __name__ == '__main__':
    main()
