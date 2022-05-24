"""

Формат ввода
В первой строке дано число вершин n (1 ≤ n ≤ 100)
и число ребер m (1 ≤ m ≤ n(n-1)). В следующих m строках
заданы ребра в виде пар вершин (u,v), если ребро ведет от u к v.

Формат вывода
Выведите информацию о рёбрах, исходящих из каждой вершины.

В строке i надо написать число рёбер, исходящих из вершины i,
а затем перечислить вершины,
в которые ведут эти рёбра –— в порядке возрастания их номеров.
"""


def main():
    num_vert, num_edg = map(int, input().split())  # кол-во вершин и рёбер
    # [count, [vertexs]] счётчик смежных и список
    vertexs = [[0, []] for i in range(num_vert)]
    # считывание и обработка рёбер
    for edge in range(num_edg):
        # вершины, соединяемые ребром
        vert_1, vert_2 = map(int, input().split())
        # для вершины vert_1 (vertexs[vert_1 - 1]) обновить список вершин
        vertexs[vert_1 - 1][0] += 1
        if vert_2 not in vertexs[vert_1 - 1][1]:
            vertexs[vert_1 - 1][1].append(vert_2)

    for vert in vertexs:
        print(vert[0], *sorted(vert[1]))


if __name__ == '__main__':
    main()
