from datetime import datetime as dt
from random import randint

tmp_arr = [None for x in range(100000)]

print('Инициализация массивов')
list_time_start = dt.now()
arr_list = [tmp_arr[i] for i in range(100000)]
list_time_1 = dt.now() - list_time_start

list_time_start = dt.now()
for count in range(1000):
    arr_list = [tmp_arr[i] for i in range(100000)]
list_time_k = (dt.now() - list_time_start) / 1000

print('list одиночный', list_time_1, 'list тысяча', list_time_k)

# dict
dict_time_start = dt.now()
arr_dict = dict()
dict_time_1 = dt.now() - dict_time_start

dict_time_start = dt.now()
for count in range(1000):
    dict_list = dict()
dict_time_k = (dt.now() - dict_time_start) / 1000

print('dict одиночный', dict_time_1, 'dict тысяча', dict_time_k)

# set
set_time_start = dt.now()
arr_set = set()
set_time_1 = dt.now() - set_time_start

set_time_start = dt.now()
for count in range(1000):
    arr_set = set()
set_time_k = (dt.now() - set_time_start) / 1000

print('set одиночный', set_time_1, 'set тысяча', set_time_k)


