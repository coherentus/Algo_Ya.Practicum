LSB = '['  # Left Square Bracket
RSB = ']'  # Right Square Bracket


def unpack_str(pack_string: str):
    # how_pack_str = len(pack_string) // 2 + 1
    # strings_accum = [''] * how_pack_str
    # accum_count = 0
    stack = []

    start_symb = -1
    string = ''
    for idx in range(len(pack_string)):
        char: str = pack_string[idx]
        if char == LSB:
            stop_symb = idx - 2
            # if stop_symb - start_symb:
            string = pack_string[start_symb:stop_symb + 1]
            if string:
                stack.append(('s', string))
            stack.append(('m', int(pack_string[idx - 1])))
            start_symb = idx + 1

        elif char == RSB:
            stop_symb = idx - 1
            string = pack_string[start_symb:stop_symb + 1]
            while stack and stack[-1][0] == 's':
                _, str_pop = stack.pop()
                string = str_pop + string
            _, mul = stack.pop()

            string = string * mul
            stack.append(('s', string))
            start_symb = idx + 1

    if stack:
        _, string = stack.pop()
        while stack:
            _, str_pop = stack.pop()
            string = str_pop + string

    return string


def get_prefix(strings):
    unp_strings = [None] * len(strings)
    for idx in range(len(strings)):
        unp_strings[idx] = unpack_str(strings[idx])

    max_prefix = 0
    stop = 0
    for col in range(len(unp_strings[0])):
        char = unp_strings[0][col]
        for row in range(1, len(unp_strings)):
            if unp_strings[row][col] != char:
                stop = 1
        if stop:
            break
        max_prefix += 1

    return unp_strings[0][0:max_prefix + 1]


def main():
    """Ввести данные, вызвать обработку, напечатать результат."""
    # ввод данных
    with open('input.txt') as file_in:
        # В первой строке записано число n (1 ≤ n ≤ 1000) –— число строк.
        # Далее в n строках записаны запакованные строки.
        num_string = int(file_in.readline())
        strings = [None] * num_string
        for i in range(num_string):
            strings[i] = file_in.readline().strip()

        print(get_prefix(strings))


if __name__ == '__main__':
    main()
