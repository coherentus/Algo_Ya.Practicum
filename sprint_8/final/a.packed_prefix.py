def unpack_str(pack_string: list):
    lsb_count = 0  # Left Square Bracket
    print(pack_string.count('['))
    return pack_string


def get_prefix(strings):
    unp_strings = [None] * len(strings)
    for idx in range(len(strings)):
        unp_strings[idx] = unpack_str(strings[idx])
        # print(len(strings[idx]))

    return len(strings)


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
