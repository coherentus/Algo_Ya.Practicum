def find_max_range(arr):
    pref_arr = [None] * len(arr)
    pref_arr[0] = arr[0]
    for i in range(1, len(arr)):
        pref_arr[i] = pref_arr[i - 1] + arr[i]

    first_val_idx = dict()
    last_val_idx = dict()

    for i in range(len(arr)):
        key = pref_arr[i]
        last_val_idx[key] = i
        if pref_arr[i] not in first_val_idx:
            first_val_idx[key] = i

    max_size = 0
    for key in first_val_idx:
        size = last_val_idx[key] - first_val_idx[key]
        if size > max_size:
            max_size = size
    return max_size


def main():
    size = int(input())
    if size:
        rounds = [None] * size
        rounds = input().split()
        for i in range(size):
            rounds[i] = -1 if rounds[i] == '0' else 1
        # list(map(int, str(input()).split()))
        print(find_max_range(rounds))
    else:
        print('0')


if __name__ == '__main__':
    main()
