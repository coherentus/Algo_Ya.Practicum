def get_max_marg(prc_arr):
    marge = 0
    for idx in range(1, len(prc_arr)):
        if prc_arr[idx] > prc_arr[idx - 1]:
            marge += prc_arr[idx] - prc_arr[idx - 1]
    return marge


def main():
    with open('input.txt') as file_in:
        # кол-во дней
        num_days = int(file_in.readline())
        prices = list(map(int, file_in.readline().split()))

        file_in.close()

    print(get_max_marg(prices))


if __name__ == '__main__':
    main()
