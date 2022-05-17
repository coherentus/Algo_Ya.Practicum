def dfs(vert_arr, num_vertex, color):  # v - номер вершины
    color[num_vertex] = 'gray'  # Вершина посещена, но ещё не обработана.
    stack = []
    print(num_vertex, end=' ')
    
    stack.append(num_vertex)
    while stack:
        fromm = stack.pop()
        if color[fromm] == 'white':
            print(fromm, end=' ')
            color[fromm] = 'gray'
        for num in vert_arr[fromm]:
            if color[num] == 'white':
                stack.append(num)
    
    """# для каждого исходящего ребра (v,w): возьмём вершину w
    for vertex in vert_arr[num_vertex]:
        if color[vertex - 1] == 'white':  # Если вершина не посещена, то
            dfs(vert_arr, vertex - 1, color)  # запустим обход от найденной смежной вершины.
    color[num_vertex] = 'black'  # Теперь вершина обработана."""
    

def main_dfs(vert_arr, start):
    # Длина массива равна числу вершин |V| + 1
    color = ['white' for i in range(len(vert_arr) + 1)]
    dfs(vert_arr, start, color)

def main():
    num_vert, num_edg = map(int, input().split())  # кол-во вершин и рёбер
    vertexs = [set() for i in range(num_vert + 1)]
    # считывание и обработка рёбер
    for _ in range(num_edg):
        # вершины, соединяемые ребром
        vert_1, vert_2 = map(int, input().split())
        # для вершины vert_1 (vertexs[vert_1 - 1]) обновить список вершин
        vertexs[vert_1].add(vert_2)
        vertexs[vert_2].add(vert_1)
        """if vert_2 not in vertexs[vert_1]:
            vertexs[vert_1].append(vert_2)
        if vert_1 not in vertexs[vert_2]:
            vertexs[vert_2].append(vert_1)"""
    for count in range(num_vert):
        vertexs[count] = sorted(vertexs[count], reverse=True)
    start_vertex = int(input())
    
    if num_vert == 1:
        print(start_vertex)
        return

    main_dfs(vertexs, start_vertex)

    
if __name__ == '__main__':
    main()
