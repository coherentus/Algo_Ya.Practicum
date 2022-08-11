def full_string(origin_string, present_arr):
    present_arr = sorted(present_arr)  # , reverse=True
    result = ''
    prev_idx = 0

    for idx, cur_str in present_arr:
        result += origin_string[prev_idx:idx]
        result += cur_str
        prev_idx = idx
    result += origin_string[prev_idx:]
    return result


def main():
    """Ввести данные, вызвать обработку, напечатать результат."""
    # ввод данных
    with open('input.txt') as file_in:
        # В первой строке дана строка s. Строка состоит из строчных букв
        # английского алфавита, не бывает пустой и её длина не превышает
        # 105 символов.
        # Во второй строке записано количество подаренных строк
        # — натуральное число n, 1 ≤ n ≤ 105.
        # В каждой из следующих n строк через пробел записаны пары ti и ki.
        # Строка ti состоит из маленьких латинских букв и не бывает пустой.
        # ki — целое число, лежащее в диапазоне от 0 до |s|.
        # Все числа ki уникальны.
        # Гарантируется, что суммарная длина всех строк ti не превосходит 105.
        origin_string = file_in.readline().strip()
        num_present = int(file_in.readline())
        present_arr = [None] * num_present
        for i in range(num_present):
            present, idx = file_in.readline().split()
            present_arr[i] = (int(idx), present)

        print(full_string(origin_string, present_arr))


if __name__ == '__main__':
    main()
