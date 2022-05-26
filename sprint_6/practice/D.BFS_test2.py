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
        tmp_arr = sorted([x for x in vert_arr[fromm] if color[x] == 'white'])
        for num in tmp_arr:
            print(num, end=' ')
            color[num] = 'gray'
            sequ.put(num)


def main_bfs(vert_arr, start):
    # Длина массива равна числу вершин |V| + 1
    color = ['white' for i in range(len(vert_arr))]
    bfs(vert_arr, start, color)


def main():
    num_vert, num_edg = map(int, input().split())  # кол-во вершин и рёбер
    vertexs_in = dict()   # [list() for i in range(num_vert + 1)]
    vertexs = [list() for i in range(num_vert + 1)]
    for _ in range(num_edg):
        vert_1, vert_2 = map(int, input().split())
        tmp = vertexs_in.get(vert_1, [])
        tmp.append(vert_2)
        vertexs_in[vert_1] = tmp
        
        """tmp = vertexs_in.get(vert_2, [])
        tmp.append(vert_1)
        vertexs_in[vert_2] = tmp"""

    for i in range(1, num_vert + 1):
        vertexs[i] = vertexs_in[i]
    
    """edges = [list() for i in range(num_edg)]
    # считывание и обработка рёбер
    for i in range(num_edg):
        # вершины, соединяемые ребром
        vert_1, vert_2 = map(int, input().split())
        
        if vert_1 < vert_2:
            edges[i] = [vert_1, vert_2]
            # vertexs[vert_1].append(vert_2)
        else:
            edges[i] = [vert_2, vert_1]
            # vertexs[vert_2].append(vert_1)

        edges = sorted(edges)
        
        init_vert = edges[0][0]
        vertexs[init_vert] = []
        for elem in edges:
            if elem[0] == init_vert:
                vertexs[init_vert].append()"""
                
            
        
    """for count in range(num_vert + 1):
        vertexs[count] = sorted(vertexs[count])"""
    start_vertex = int(input())

    if num_vert == 1:
        print(start_vertex)
        return

    main_bfs(vertexs, start_vertex)


if __name__ == '__main__':
    main()
