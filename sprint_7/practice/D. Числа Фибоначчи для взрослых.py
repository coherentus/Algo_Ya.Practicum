def get_fib(number):
    prev_1 = 1
    prev_2 = 1
    cur_num = 2
    while cur_num <= number:
        cur_num += 1
        cur_fib = (prev_1 + prev_2) % 1000000007
        prev_1, prev_2 = prev_2, cur_fib
    return cur_fib


def main():
    """Ввести данные, вызвать обработку, напечатать результат."""
    # ввод данных
    with open('input.txt') as file_in:
        # В единственной строке дано целое число n (0 ≤ n ≤ 106)
        # Вычислите значение Fn по модулю 109 + 7 и выведите его
        number = int(file_in.readline())
        print(get_fib(number))

if __name__ == '__main__':
    main()
