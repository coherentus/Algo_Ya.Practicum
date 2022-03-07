def find_sums(arr, nums, need_sum):
    result = list()
    res_str = dict()
    for pos_1 in range(0, len(arr) - 3):
        str_1 = arr[pos_1]
        sum_1 = nums[pos_1]
        for pos_2 in range(pos_1 + 1, len(arr) - 2):
            str_2 = arr[pos_2]
            sum_2 = sum_1 + nums[pos_2]
            for pos_3 in range(pos_2 + 1, len(arr) - 1):
                str_3 = arr[pos_3]
                sum_3 = sum_2 + nums[pos_3]
                for pos_4 in range(pos_3 + 1, len(arr)):
                    str_4 = arr[pos_3]
                    sum_4 = sum_3 + nums[pos_4]
                    if sum_4 == need_sum:
                        cur_candid = sorted([
                            arr[pos_1],
                            arr[pos_2],
                            arr[pos_3],
                            arr[pos_4],
                        ])
                        res_str[tuple(sorted([str_1, str_2, str_3, str_4]))] = cur_candid
                        
    return sorted(res_str.values())


def main():
    count_nums = int(input())
    needed_sum = int(input())
    if count_nums:
        nums_arr = [None] * count_nums
        input_arr = [None] * count_nums
        idx = 0
        for in_num in input().split():
            input_arr[idx] = in_num
            nums_arr[idx] = int(in_num)
            idx += 1
        answer = find_sums(input_arr, nums_arr, needed_sum)
        print(len(answer))
        for answ in answer:
            print(*answ)
    else:
        print('0')


if __name__ == '__main__':
    main()
