from queue import Queue


def bfs(vert_arr, num_vertex, color):  # v - номер вершины
    # color[num_vertex] = 'gray'  # Вершина посещена, но ещё не обработана.
    # print(num_vertex, end=' ')

    sequ = Queue(100000 + 1)
    sequ.put(num_vertex)
    print(num_vertex, end=' ')
    color[num_vertex] = 'gray'  # Вершина посещена, но ещё не обработана.

    while not sequ.empty():
        fromm = sequ.get()
        step_vertexs = list()
        for num in vert_arr[fromm]:
            if color[num] == 'white':
                # print(num, end=' ')
                color[num] = 'gray'
                step_vertexs.append(num)
                sequ.put(num)
        print(*step_vertexs, end=' ')


def main_bfs(vert_arr, start):
    # Длина массива равна числу вершин |V| + 1
    color = ['white' for i in range(len(vert_arr))]
    bfs(vert_arr, start, color)


def main():
    num_vert, num_edg = map(int, input().split())  # кол-во вершин и рёбер
    vertexs = [list() for i in range(num_vert + 1)]  # set()
    # считывание и обработка рёбер
    for _ in range(num_edg):
        # вершины, соединяемые ребром
        vert_1, vert_2 = map(int, input().split())
        # для вершины vert_1 (vertexs[vert_1 - 1]) обновить список вершин
        vertexs[vert_1].append(vert_2)
        vertexs[vert_2].append(vert_1)

    """for count in range(num_vert + 1):
        vertexs[count] = sorted(vertexs[count])"""
    start_vertex = int(input())

    if num_vert == 1:
        print(start_vertex)
        return

    main_bfs(vertexs, start_vertex)


if __name__ == '__main__':
    main()
