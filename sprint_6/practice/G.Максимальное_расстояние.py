from queue import Queue


def max_distance(vert_arr, start_vert):

    # Длины массивов равны числу вершин|V| + 1.
    color = ['white'] * len(vert_arr)
    distance = [0] * len(vert_arr)
    max_dist = 0
    # dists_set = set()

    # Создадим очередь вершин и положим туда стартовую вершину.
    planned = Queue()
    planned.put(start_vert)
    color[start_vert] = 'gray'
    distance[start_vert] = 0
    # dists_set.add(distance[start_vert])

    while not planned.empty():

        # Возьмём вершину из очереди.
        cur_vert_num = planned.get()
        cur_vert_arr = vert_arr[cur_vert_num]
        print(cur_vert_arr)

        for vertex_num in cur_vert_arr:

            if color[vertex_num] == 'white':
                color[vertex_num] = 'gray'
                cur_dist = distance[cur_vert_num] + 1
                distance[vertex_num] = cur_dist
                # dists_set.add(distance[vertex_num])
                if cur_dist > max_dist:
                    max_dist = cur_dist
                planned.put(vertex_num)  # Запланируем посещение вершины.
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
