def find_max_cost(piece_arr, weight):
    return len(piece_arr, weight)


def main():
    """Ввести данные, вызвать обработку, напечатать результат."""
    # ввод данных
    with open('input.txt') as file_in:
        # В первой строке дано число слитков —– натуральное число n (1 ≤ n ≤ 1000)
        # и вместимость рюкзака –— целое число M (0 ≤ M ≤ 104).
        num_piece, max_weight = map(int, file_in.readline().split())

        # Во второй строке записано n натуральных чисел
        # wi (1 ≤ wi ≤ 104) -— массы слитков.
        # считывание слитков
        pieces = map(int, file_in.readline().split())

    print(find_max_cost(pieces, max_weight))


if __name__ == '__main__':
    main()
