def find_max_cost(piece_arr, weight):
    # массив накопления признаков сумм
    dp = [False] * (weight + 1)
    dp[0] = True

    # перебирая эл-ты от piece_arr[0] до pieces_arr[-1] в массиве dp будут
    # ставится 'True' на местах всех возможных сумм из просматриваемых
    # эл-тов.
    # индекс самой правой True - искомый максимум.
    for idx_elem in range(len(piece_arr)):
        cur_elem = piece_arr[idx_elem]

        for idx_dp in range(weight, cur_elem - 1, -1):
            if dp[idx_dp - cur_elem]:
                dp[idx_dp] = True
    for idx in range(len(dp) - 1, 0, -1):
        if dp[idx]:
            return idx


def main():
    """Ввести данные, вызвать обработку, напечатать результат."""
    # ввод данных
    with open('input.txt') as file_in:
        # В первой строке дано число слитков —–
        # натуральное число n (1 ≤ n ≤ 1000)
        # и вместимость рюкзака –— целое число M (0 ≤ M ≤ 104).
        num_piece, max_weight = map(int, file_in.readline().split())
        if num_piece and max_weight:
            # Во второй строке записано n натуральных чисел
            # wi (1 ≤ wi ≤ 104) -— массы слитков.
            # считывание слитков
            pieces = list(map(int, file_in.readline().split()))
            print(find_max_cost(pieces, max_weight))
        else:
            print('0')


if __name__ == '__main__':
    main()
