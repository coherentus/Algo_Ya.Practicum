def find_sums(arr,  need_sum):
    result = list()
    sums2_dict = {}
    # суммы двоек
    for pos_1 in range(0, len(arr) - 1):
        for pos_2 in range(pos_1 + 1, len(arr)):
            sum2 = arr[pos_1] + arr[pos_2]
            if sum2 in sums2_dict:
                tmp = sums2_dict[sum2]
                tmp.append((pos_1, pos_2))
                sums2_dict[sum2] = tmp
            else:
                sums2_dict[sum2] = [(pos_1, pos_2)]

    for key in sums2_dict:
        degree_4 = need_sum - key
        if degree_4 in sums2_dict:
            first_2 = sums2_dict[key]
            second_2 = sums2_dict[degree_4]
            for pos_1 in first_2:
                for pos_2 in second_2:
                    candid = list(pos_1) + list(pos_2)
                    if len(set(candid)) == len(candid):
                        res_nums = [arr[x] for x in candid]
                        result.append(tuple(sorted(res_nums)))

    return sorted(set(result))


def main():
    count_nums = int(input())
    needed_sum = int(input())
    if count_nums:
        input_arr = [None] * count_nums
        idx = 0
        for in_num in input().split():
            input_arr[idx] = int(in_num)
            idx += 1
        answer = find_sums(input_arr, needed_sum)
        print(len(answer))
        for answ in answer:
            print(*answ)
    else:
        print('0')


if __name__ == '__main__':
    main()
