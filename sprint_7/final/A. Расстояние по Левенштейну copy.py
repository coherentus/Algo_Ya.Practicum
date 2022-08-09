def get_levenshtein(string_one, string_two):
    # между идентичными строками расстояние равно нулю
    if string_one == string_two:
        return 0
    
    # если одна строка пуста, то расстояние равно длине другой строки
    if not (string_one and string_two):
        return max(len(string_one), len(string_two))
    
    # для удобства работы алгоритма первой строкой берётся более короткая
    if len(string_two) < len(string_one):
        string_one, string_two = string_two, string_one
    
    str_1, str_2 = string_one, string_two
    n, m = len(string_one), len(string_two)
    if n > m:
        str_1, str_2 = string_two, string_one
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]


def main():
    with open('input.txt') as file_in:
        first_string = file_in.readline()
        second_string = file_in.readline()
        file_in.close()

    print(get_levenshtein(first_string, second_string))


if __name__ == '__main__':
    main()
