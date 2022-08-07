def get_components(vert_arr):

    count_comp = 0
    components_arr = list()

    visited = ['white' for _ in range(len(vert_arr))]

    for vert in range(1, len(vert_arr)):
        if visited[vert] == 'white':
            count_comp += 1
            components_arr.append([])

            visited[vert] = 'gray'  # Вершина посещена, но ещё не обработана.
            components_arr[count_comp - 1].append(vert)

            stack = []
            for num in vert_arr[vert]:
                if visited[num] == 'white':
                    stack.append(num)

            while stack:
                fromm = stack.pop()
                if visited[fromm] == 'white':

                    components_arr[count_comp - 1].append(fromm)
                    visited[fromm] = 'gray'
                    for num in vert_arr[fromm]:
                        if visited[num] == 'white':
                            stack.append(num)

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
        print(*sorted(component))


if __name__ == '__main__':
    main()
