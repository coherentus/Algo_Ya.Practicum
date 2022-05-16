def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)

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

    dfs(vertexs, start_vertex)

    
if __name__ == '__main__':
    main()
