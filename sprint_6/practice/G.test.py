from queue import Queue


def max_distance(vert_arr, start_vert):

    frontier = Queue()
    frontier.put(start_vert)
    visited = {}
    visited[start_vert] = True
    distance = {}
    distance[start_vert] = 0
    max_dist = 0

    while not frontier.empty():
        current = frontier.get()
        for next in vert_arr[current]:
            if next not in visited:
                frontier.put(next)
                visited[next] = True
                distance[next] = distance[current] + 1
                if distance[next] > max_dist:
                    max_dist = distance[next]
            
    return max_dist

def main():
    
    with open('input.txt') as file_in:
        # кол-во вершин и рёбер
        num_vert, num_edg = file_in.readline().split()
        num_vert, num_edg = int(num_vert), int(num_edg)
        vertexs = [list() for _ in range(num_vert + 1)]
        # считывание и обработка рёбер
        for _ in range(num_edg):
            # вершины, соединяемые ребром
            vert_1, vert_2 = file_in.readline().split()
            vert_1, vert_2 = int(vert_1), int(vert_2)
            
            vertexs[vert_2].append(vert_1)
            vertexs[vert_1].append(vert_2)
            
        """for _ in range(len(vertexs)):
            vertexs[_] = sorted(vertexs[_])"""
        
        
        start_vertex = int(file_in.readline())
        file_in.close()

    if num_vert == 1:
        print('0')
        return

    print(max_distance(vertexs, start_vertex))


if __name__ == '__main__':
    main()
