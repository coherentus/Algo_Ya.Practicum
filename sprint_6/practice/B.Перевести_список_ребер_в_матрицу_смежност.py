"""

Формат ввода
В первой строке дано число вершин n (1 ≤ n ≤ 100)
и число рёбер m (1 ≤ m ≤ n(n-1)).
В следующих m строках заданы ребра в виде пар вершин (u,v),
если ребро ведет от u к v.

Формат вывода
Выведите матрицу смежности n на n.
На пересечении i-й строки и j-го столбца стоит единица,
если есть ребро, ведущее из i в j.
"""


def main():
    num_vert, num_edg = map(int, input().split())  # кол-во вершин и рёбер
    matrix = [[0 for j in range(num_vert)] for i in range(num_vert)]
    # считывание и обработка рёбер
    for edge in range(num_edg):
        vert_1, vert_2 = map(int, input().split())
        matrix[vert_1 - 1][vert_2 - 1] = 1

    for row in matrix:
        print(*row)


if __name__ == '__main__':
    main()
