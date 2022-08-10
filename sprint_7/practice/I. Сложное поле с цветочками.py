def get_quantity(matrix, rows_num, cols_num):
    path = ''
    for row_idx in range(rows_num - 1, -1, -1):
        for col_idx in range(1, cols_num + 1):
            matrix[row_idx][col_idx] = (
                matrix[row_idx][col_idx]
                + max(
                    matrix[row_idx][col_idx - 1],
                    matrix[row_idx + 1][col_idx]
                )
            )

    col_idx = cols_num  # x
    row_idx = 0
    while (row_idx != rows_num - 1 or col_idx != 1):
        if col_idx == 1:
            path += 'U'
            row_idx += 1
            continue

        down = matrix[row_idx + 1][col_idx]
        left = matrix[row_idx][col_idx - 1]

        if down > left:
            row_idx += 1
            path += 'U'
        else:
            col_idx -= 1
            path += 'R'

    return matrix[0][cols_num], path[::-1]


def main():
    with open('input.txt') as file_in:
        # В первой строке даны размеры поля n и m (через пробел).
        # Оба числа лежат в диапазоне от 1 до 1000.
        # В следующих n строках задано поле. Каждая строка состоит
        # из m символов 0 или 1, записанных подряд без пробелов,
        # и завершается переводом строки. Если в клетке записана единица,
        # то в ней растёт цветочек.
        rows_num, cols_num = list(map(int, file_in.readline().split()))
        matrix = [[0] * (cols_num + 1) for _ in range(rows_num + 1)]
        for i in range(rows_num):
            in_line = file_in.readline()
            for j in range(cols_num):
                if in_line[j] == '1':
                    matrix[i][j + 1] = 1

        file_in.close()

    quanty, path = get_quantity(matrix, rows_num, cols_num)
    print(quanty)
    print(path)


if __name__ == '__main__':
    main()
