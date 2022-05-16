def dfs(vert_arr, num_vertex, color):  # v - номер вершины
    color[num_vertex] = 'gray'  # Вершина посещена, но ещё не обработана.
    # для каждого исходящего ребра (v,w): возьмём вершину w
    for vertex in vert_arr[num_vertex]:
        if color[vertex - 1] == 'white':  # Если вершина не посещена, то
            dfs(vert_arr, vertex - 1, color)  # запустим обход от найденной смежной вершины.
    color[num_vertex] = 'black'  # Теперь вершина обработана.
    print(num_vertex + 1, end=' ')

def main_dfs(vert_arr, start):
    # Длина массива равна числу вершин |V|
    color = ['white' for i in range(len(vert_arr))]
    
    dfs(vert_arr, start, color)

def main():
    num_vert, num_edg = map(int, input().split())  # кол-во вершин и рёбер
    vertexs = [[] for i in range(num_vert)]
    # считывание и обработка рёбер
    for _ in range(num_edg):
        # вершины, соединяемые ребром
        vert_1, vert_2 = map(int, input().split())
        # для вершины vert_1 (vertexs[vert_1 - 1]) обновить список вершин
        if vert_2 not in vertexs[vert_1 - 1]:
            vertexs[vert_1 - 1].append(vert_2)
        """if vert_1 not in vertexs[vert_2 - 1]:
            vertexs[vert_2 - 1].append(vert_1)"""
    for count in range(num_vert):
        vertexs[count] = sorted(vertexs[count])
    start_vertex = int(input())
    if num_vert == 1:
        print(start_vertex)

    main_dfs(vertexs, start_vertex)

    
if __name__ == '__main__':
    main()
