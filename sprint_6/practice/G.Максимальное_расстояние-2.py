from queue import Queue


def get_distance(vert_arr, start_vert):
    # bfs
    visited = [False] * len(vert_arr)
    visited[start_vert] = True
    q = Queue()
    q.put((start_vert, 1))
    
    result = 0
    
    while not q.empty():
        item_vert, item_weight = q.get()
        
        
        """if item_vert == end_vert:
            return item_weight -1"""
        
        for too in vert_arr[item_vert]:
            if not visited[too]:
                result = max(result, item_weight)
                visited[too] = True
                q.put((too, item_weight + 1))    
    
    return result


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

        # вершины для нахождения расстояния
        from_vert = int(file_in.readline())

        file_in.close()

    print(get_distance(vertexs, from_vert))


if __name__ == '__main__':
    main()
