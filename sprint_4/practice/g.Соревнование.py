def find_long_range(arr, start):
    """Вернуть длину последовательности.

    """
    result = 0
    idx = start
    parity = 0  # zero - is parity, not zero - not parity
    while idx < len(arr) - 1:  # out of range guard
        parity = parity + 1 if arr[idx] else parity - 1
        parity = parity + 1 if arr[idx + 1] else parity - 1
        idx += 2
        if not parity:
            result += idx - start
    return result


def find_max_range(arr):
    max_len = 0
    for i in range(len(arr)):
        loc_start = i
        if max_len < len(arr) - i:
            cur_len = find_long_range(arr, loc_start)
            if cur_len > max_len:
                max_len = cur_len
            loc_start += cur_len

    return max_len


def main():
    if int(input()):
        rounds = list(map(int, str(input()).split()))
        print(find_max_range(rounds))
    else:
        print('0')


if __name__ == '__main__':
    main()
