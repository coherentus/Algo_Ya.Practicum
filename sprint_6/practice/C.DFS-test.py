def dfs(graph, start, colors):  # visited=None
    """if visited is None:
        visited = set()
    visited.add(start)"""
    print(start, end=' ')
    colors[start] = 'gray'
    next_set = sorted(x for x in graph[start] if colors[x] == 'white')  # graph[start] - visited
    for next in next_set:
        dfs(graph, next, colors)

def main():
    num_vert, num_edg = map(int, input().split())  # кол-во вершин и рёбер
    vertexs = [set() for i in range(num_vert + 1)]
    color = ['white' for i in range(num_vert + 1)]
    # считывание и обработка рёбер
    for _ in range(num_edg):
        # вершины, соединяемые ребром
        vert_1, vert_2 = map(int, input().split())
        # для вершины vert_1 (vertexs[vert_1 - 1]) обновить список вершин
        vertexs[vert_1].add(vert_2)
        vertexs[vert_2].add(vert_1)
    start_vertex = int(input())

    if num_vert == 1:
        print(start_vertex)
    else:
        dfs(vertexs, start_vertex, color)

    
if __name__ == '__main__':
    main()
