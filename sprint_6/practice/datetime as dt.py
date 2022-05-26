from datetime import datetime as dt
from random import randint

SIZE_E = 100000
SIZE_V = 100000

tmp_arr = [None for x in range(SIZE_E)]

for i in range(SIZE_E):
    tmp_arr[i] = randint(1, SIZE_V - 1), randint(1, SIZE_V - 1)

arr_list = [list() for x in range(SIZE_V)]
arr_dict = dict()
arr_set = [set() for x in range(SIZE_V)]

# list
time_list = dt.now()
for edge in tmp_arr:
    arr_list[edge[0]].append(edge[1])
    arr_list[edge[1]].append(edge[0])
time_list_1 = dt.now() - time_list
for i in range(SIZE_V):
    arr_list[i] = sorted(arr_list[i])
print('time_list sorted:', time_list_1)

# dict
time_dict = dt.now()
for edge in tmp_arr:
    tmp = arr_dict.get(edge[0], [])
    tmp.append(edge[1])
    arr_dict[edge[0]] = tmp
    
    tmp = arr_dict.get(edge[1], [])
    tmp.append(edge[0])
    arr_dict[edge[1]] = tmp

for key, value in arr_dict.items():
    tmp = arr_dict[key]
    arr_dict[key] = sorted(tmp)
time_dict_1 = dt.now() - time_dict
print('time_dict :', time_dict_1)

# set
time_set = dt.now()
for edge in tmp_arr:
    arr_set[edge[0]].add(edge[1])
    arr_set[edge[1]].add(edge[0])
for i in range(SIZE_V):
    arr_set[i] = sorted(arr_set[i])
time_set_1 = dt.now() - time_set
print('time_set :', time_set_1)



# print(tmp_arr)
# print(*tmp_arr)
