count_in = int(input())
dict_in = dict()
for i in range(count_in):
    cur_in = input()
    if cur_in not in dict_in:
        dict_in[cur_in] = True
        print(cur_in)
