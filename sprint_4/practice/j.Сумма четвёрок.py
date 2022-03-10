import bisect

def find_sums(nums, need_sum):
    result = list()
    res_str = dict()
    for pos_1 in range(0, len(nums) - 3):
        #str_1 = arr[pos_1]
        #sum_1 = nums[pos_1]
        for pos_2 in range(pos_1 + 1, len(nums) - 2):
            #str_2 = arr[pos_2]
            #sum_2 = sum_1 + nums[pos_2]
            for pos_3 in range(pos_2 + 1, len(nums) - 1):
                #str_3 = arr[pos_3]
                #sum_3 = sum_2 + nums[pos_3]
                sum_4 = need_sum - sum([nums[pos_1], nums[pos_2], nums[pos_3]])
                pos_4 = pos_3 + 1
                
                if sum_4 in nums[pos_4:]:
                    candid = [nums[pos_1], nums[pos_2], nums[pos_3], nums[pos_4]]
                    cur_candid = tuple(sorted(candid))
                    result.append(cur_candid)
            
                
                
                """while pos_4 < len(nums):
                    pos_4 = bisect.bisect_left(nums, sum_4, lo=pos_4)
                    if pos_4 != len(nums) and nums[pos_4] == sum_4:
                        candid = [nums[pos_1], nums[pos_2], nums[pos_3], nums[pos_4]]
                        cur_candid = tuple(sorted(candid))
                        result.append(cur_candid)
                        pos_4 += 1
                        continue
                    else:
                        break
                    
                
                
                for pos_4 in range(pos_3 + 1, len(nums)):
                    #str_4 = arr[pos_4]
                    candid = [nums[pos_1], nums[pos_2], nums[pos_3], nums[pos_4]]
                    sum_4 = sum(candid)
                    if sum_4 == need_sum:
                        cur_candid = tuple(sorted(candid))
                        #print(cur_candid)
                        result.append(cur_candid)
                        #res_str[tuple(cur_candid)] = cur_candid"""
                        
    return sorted(set(result))


def main():
    count_nums = int(input())
    needed_sum = int(input())
    if count_nums:
        #nums_arr = [None] * count_nums
        #input_arr = [None] * count_nums
        nums_arr = list(map(int, input().split()))
        """idx = 0
        for in_num in input().split():
            #input_arr[idx] = in_num
            nums_arr[idx] = int(in_num)
            idx += 1"""
        answer = find_sums(nums_arr, needed_sum)
        print(len(answer))
        for answ in answer:
            print(*answ)
    else:
        print('0')


if __name__ == '__main__':
    main()
