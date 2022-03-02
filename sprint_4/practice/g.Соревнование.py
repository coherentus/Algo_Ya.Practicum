def chek_range(arr, start, size):
    if sum(arr[start: start + size:]) == size // 2:
        return True
    return False


def find_long_range(arr, first):
    len_range = 0
    start = first
    size = 2
    while (size + start) < len(arr) + 1:
        if chek_range(arr, start, size):
            len_range += size
            start += size
            size *= 2
        else:
            return len_range
    return len_range


def find_max_range(arr):
    max_range = 0
    for i in range(len(arr)):
        cur_range = find_long_range(arr, i)
        if cur_range > max_range:
            max_range = cur_range
    return max_range


def main():
    if int(input()):
        rounds = list(map(int, str(input()).split()))
        print(find_max_range(rounds))
    else:
        print('0')


if __name__ == '__main__':
    main()
