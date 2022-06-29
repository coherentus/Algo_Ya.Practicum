from queue import Queue

def dfs(vert_arr, num_vertex):  # v - номер вершины
    color = ['white' for i in range(len(vert_arr) + 1)]
    color[num_vertex] = 'gray'  # Вершина посещена, но ещё не обработана.
    result = list()
    result.append(num_vertex)

    stack = []
    for num in vert_arr[num_vertex]:
        if color[num] == 'white':
            stack.append(num)

    while stack:
        fromm = stack.pop()
        if color[fromm] == 'white':
            result.append(fromm)
            color[fromm] = 'gray'
            for num in vert_arr[fromm]:
                if color[num] == 'white':
                    stack.append(num)

    return result

def get_components(vert_arr):
    vert_arr = sorted(vert_arr)
    count_comp = 0
    components_arr = list()
    # набор номеров всех вершин
    full_vert_numbers = set([x for x in range(1, len(vert_arr) + 1)])
    start_vert = 1
    
    while full_vert_numbers:
        cur_comp = dfs(vert_arr, start_vert)
        components_arr.append(cur_comp)
        count_comp += 1
        full_vert_numbers -= set(cur_comp)
        start_vert = list(full_vert_numbers)[0]
    

    return count_comp, components_arr

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

        file_in.close()

    components_count, components = get_components(vertexs)
    print(components_count)
    for component in components:
        print(component)


if __name__ == '__main__':
    main()
