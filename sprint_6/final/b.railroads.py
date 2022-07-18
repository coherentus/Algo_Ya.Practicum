def check_optimum(towns_arr):
    pass


def main():
    """Ввести данные, вызвать обработку, напечатать результат.


    """
    # ввод данных
    with open('input.txt') as file_in:
        # кол-во городов
        num_towns = int(file_in.readline())

        # Карта задана n-1 строкой.
        # В i-й строке описаны дороги из города i в города i+1, i+2, ..., n.
        # В строке записано n - i символов, каждый из которых либо R, либо B.
        # Если j-й символ строки i равен «B»,
        # то из города i в город i + j идет дорога типа «B». Аналогично для типа «R».

        towns = ['' for _ in range(num_towns + 1)]
        # считывание и обработка дорог
        for town_count in range(1, num_towns):
            towns[town_count] = file_in.readline().strip()
        file_in.close()

    print(check_optimum(towns))


if __name__ == '__main__':
    main()
