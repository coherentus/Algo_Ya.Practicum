def binary_view(bin1, bin2):
    """Вернуть двоичное представление суммы двоичных входных чисел.

    Args:
        bin1 (str): строка с первым числом
        bin2 (str): строка со вторым числом

    Returns:
        str: строка суммы

    Работа ведётся со строками и символами.
    Для удобства входные строки разворачиваются.
    Формирование ответа начинается с младшего разряда.
    В определении символа разряда участвуют три символа пока в более
    коротком числе есть разряды, далее два, признак переполнения и
    символы из чисел.
    """
    # min_len = len(bin1)
    if len(bin1) > len(bin2):
        min_len = len(bin2)
        max_len = len(bin1)
        min_bin = bin2
        max_bin = bin1
    else:
        min_len = len(bin1)
        max_len = len(bin2)
        min_bin = bin1
        max_bin = bin2

    min_bin_r = ''.join(reversed(min_bin))
    max_bin_r = ''.join(reversed(max_bin))
    result = ''
    digit = ''
    append_flag = '0'
    for i in range(min_len):
        # str bin1 bin2 app_flag
        digit = min_bin_r[i] + max_bin_r[i] + append_flag
        # four possible combinations based on the results
        # res_digit     app_flag    combinations
        #   0           0           '000'
        #   1           0           '100' '010' '001'
        #   0           1           '110' '101' '011'
        #   1           1           '111'
        if digit == '000':
            result = '0' + result
            append_flag = '0'

        elif (digit == '100' or digit == '010' or digit == '001'):
            result = '1' + result
            append_flag = '0'

        elif (digit == '110' or digit == '101' or digit == '011'):
            result = '0' + result
            append_flag = '1'

        else:
            # digit == '111':
            result = '1' + result
            append_flag = '1'

    for i in range(min_len, max_len):
        digit = max_bin_r[i] + append_flag
        # res_digit     app_flag    combinations
        #   0           0           '00'
        #   1           0           '10' '01'
        #   0           1           '11'
        if digit == '00':
            result = '0' + result
            append_flag = '0'
        elif (digit == '10' or digit == '01'):
            result = '1' + result
            append_flag = '0'
        else:
            # digit == '11'
            result = '0' + result
            append_flag = '1'

    if append_flag == '1':
        result = '1' + result
    return result


def main():
    bin_one = str(input())
    bin_two = str(input())

    print(binary_view(bin_one, bin_two))


if __name__ == '__main__':
    main()
