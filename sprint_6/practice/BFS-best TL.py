import sys
from queue import Queue


def main_bfs(vert_arr, num_vertex):  # num_vertex - номер вершины
    result = [None] * len(vert_arr)
    res_count = 0
    color = ['white' for _ in range(len(vert_arr) + 1)]
    
    
    """print(num_vertex, end=' ')"""
    result[res_count] = num_vertex

    """sequ = []
    for num in vert_arr[num_vertex]:
        if color[num] == 'white':
            sequ.append(num)"""
    sequ = Queue(100000 + 1)
    sequ.put(num_vertex)
    color[num_vertex] = 'gray'  # Вершина посещена, но ещё не обработана.

    while not sequ.empty():
        fromm = sequ.get()
        for num in vert_arr[fromm]:
            if color[num] == 'white':
                """print(num, end=' ')"""
                res_count += 1
                result[res_count] = fromm
                color[num] = 'gray'
                sequ.put(num)
    
    
    
    
    """while sequ:
        fromm = sequ.pop(0)
        if color[fromm] == 'white':
            
            #print(fromm, end=' ')
            res_count += 1
            result[res_count] = fromm
            
            color[fromm] = 'gray'
            for num in vert_arr[fromm]:
                if color[num] == 'white':
                    sequ.append(num)"""

    return result


def main():
    num_vert, num_edg = map(int, input().split())  # кол-во вершин и рёбер
    vertexs = [set() for _ in range(num_vert + 1)]
    # считывание и обработка рёбер
    for _ in range(num_edg):
        # вершины, соединяемые ребром
        """vert_1, vert_2 = map(int, input().split())"""
        line = sys.stdin.readline().rstrip()
        vert_1, vert_2 = line.split()
        vert_1, vert_2 = int(vert_1), int(vert_2)
        # для вершины vert_1 (vertexs[vert_1 - 1]) обновить список вершин
        vertexs[vert_1].add(vert_2)
        #vertexs[vert_2].add(vert_1)

    for count in range(num_vert + 1):
        vertexs[count] = sorted(vertexs[count])
    start_vertex = int(input())

    if num_vert == 1:
        print(start_vertex)
        return

    result = main_bfs(vertexs, start_vertex)
    for res in result:
        if res:
            print(res, end=' ')


if __name__ == '__main__':
    main()
