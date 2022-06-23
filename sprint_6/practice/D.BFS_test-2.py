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
        for num in vert_arr[fromm]:
            if color[num] == 'white':
                print(num, end=' ')
                color[num] = 'gray'
                sequ.put(num)


def main_bfs(vert_arr, start):
    # Длина массива равна числу вершин |V| + 1
    color = ['white' for i in range(len(vert_arr))]
    bfs(vert_arr, start, color)


def main():
    num_vert, num_edg = map(int, input().split())  # кол-во вершин и рёбер
    vertexs = [set() for i in range(num_vert + 1)]
    # считывание и обработка рёбер
    edges = [None for i in range(num_edg)] 
    for edge in range(num_edg):
        edges[edge] = list(map(int, input().split()))
    edges = sorted(edges)

    for edge in edges:
        vertexs[edge[0]].add(edge[1])
        vertexs[edge[1]].add(edge[0])

    """for count in range(num_vert + 1):
        vertexs[count] = sorted(vertexs[count])"""
    start_vertex = int(input())

    if num_vert == 1:
        print(start_vertex)
        return

    main_bfs(vertexs, start_vertex)


if __name__ == '__main__':
    main()


trr = dict(one = [1, 2, 3])
trr['one'] = (trr['one'].append(5))