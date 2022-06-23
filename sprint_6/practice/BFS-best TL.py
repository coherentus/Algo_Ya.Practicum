from queue import Queue


def main_bfs(vert_arr, num_vertex):
    # Длина массива равна числу вершин |V| + 1
    color = ['white' for _ in range(len(vert_arr))]
    color[num_vertex] = 'gray'  # Вершина посещена, но ещё не обработана.
    """print(num_vertex, end=' ')"""
    res_out = [None] * len(vert_arr)
    res_out_count = 0
    res_out[res_out_count] = num_vertex

    # sequ = []
    sequ = Queue(len(vert_arr))
    
    for num in vert_arr[num_vertex]:
        if color[num] == 'white':
            sequ.put(num)

    while not sequ.empty():
        fromm = sequ.get()
        if color[fromm] == 'white':
            """print(fromm, end=' ')"""
            res_out_count += 1
            res_out[res_out_count] = fromm
            color[fromm] = 'gray'
            
            for num in vert_arr[fromm]:
                if color[num] == 'white':
                    sequ.put(num)

    return [value for value in res_out if value]

def main():
    with open('input.txt') as file_in:
        """num_vert, num_edg = map(int, input().split())  # кол-во вершин и рёбер"""
        num_vert, num_edg = file_in.readline().split()
        num_vert, num_edg = int(num_vert), int(num_edg)
        vertexs = [list() for _ in range(num_vert + 1)]
        # считывание и обработка рёбер
        for _ in range(num_edg):
            # вершины, соединяемые ребром

            """vert_1, vert_2 = map(int, input().split())"""
            """line = sys.stdin.readline().rstrip()"""
            
            vert_1, vert_2 = file_in.readline().split()
            vert_1, vert_2 = int(vert_1), int(vert_2)
            
            vertexs[vert_2].append(vert_1)
            vertexs[vert_1].append(vert_2)
            

        """for count in range(num_vert + 1):
            vertexs[count] = sorted(vertexs[count])"""
        vertexs = sorted(vertexs)
        
        """start_vertex = int(input())"""
        start_vertex = int(file_in.readline())
        file_in.close()

    if num_vert == 1:
        print(start_vertex)
        return

    """print(*main_bfs(vertexs, start_vertex))"""
    result = main_bfs(vertexs, start_vertex)
    with open('output.txt', 'w') as file_out:        
        file_out.write(*result)
        file_out.close()


if __name__ == '__main__':
    main()
