def main():
    # ввод данных
    with open('input.txt') as file_in:
        # кол-во вершин и рёбер
        num_vert, num_edg = file_in.readline().split()
        num_vert, num_edg = int(num_vert), int(num_edg)
        
        edges = [list() for _ in range(num_edg)]
        # считывание и обработка рёбер
        for _ in range(num_edg):
            # вершины, соединяемые ребром и вес этого ребра
            vert_1, vert_2, weight = file_in.readline().split()
            vert_1, vert_2, weight = int(vert_1), int(vert_2), int(weight)
            
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
