ERROR_MESSAGE = 'Oops! I did it again'


def max_weight(edges_full):
    def extract_max(edges):
        # найти ребро с максимальным весом,
        # удалить из edges и вернуть
        max_e = edges[0]
        for edge in edges:
            if max_e['weight'] > edge['weight']:
                max_e = edge
        edges.remove(max_e)
        return max_e

    maximum = 0
    
    minimum_spanning_tree = []   # Рёбра, составляющие MST.

    added = set()          # Множество вершин, уже добавленных в остов.
    not_added = set()      # Множество вершины, ещё не добавленных в остов. 
    edges = []          # Массив рёбер, исходящих из остовного дерева.

    """not_added = graph.vertices"""
    for item in edges_full:
        not_added.add(item['start'])
        not_added.add(item['end'])
    
    # Берём первую попавшуюся вершину.
    v = 1
    added.add(v)
    not_added.remove(v)
    edges_v = list()
    for edge in edges_full:
        if edge['start'] == v and edge['end'] in not_added:
            edges.append(edge)
            edges_full.remove(edge)
            
    """edges += graph.edges.filter(start == v, end in not_added)"""
    

    """пока not_added не пуст и edges не пуст:"""
    while (not_added and edges):
        # Подразумеваем, что extract_minimum извлекает минимальное ребро 
        # из массива рёбер и больше данного ребра в массива не будет.
        e = extract_max(edges)
        e_end = e['end']
        if e_end in not_added:
            minimum_spanning_tree.append(e)
        added.add(e_end)
        not_added.remove(e_end)
        edges_v = list()
        for edge in edges_full:
            if edge['start'] == e_end and edge['end'] in not_added:
                edges.append(edge)
                edges_full.remove(edge)

    if not_added: 
        return ERROR_MESSAGE
    else:
        return sum([_['weight'] for _ in minimum_spanning_tree])


def main():
    """
    
    Граф вводится в структуру вида:
    edges = [
        {start: NN, end: MM, weight: XX},
    ]
    """
    # ввод данных
    with open('input.txt') as file_in:
        # кол-во вершин и рёбер
        num_vert, num_edg = file_in.readline().split()
        num_vert, num_edg = int(num_vert), int(num_edg)
        if num_vert - num_edg > 1:
            print(ERROR_MESSAGE)
            return
            
        
        edges = [None for _ in range(num_edg)]
        # считывание и обработка рёбер
        for _ in range(num_edg):
            # вершины, соединяемые ребром и вес этого ребра
            vert_1, vert_2, weight = file_in.readline().split()
            vert_1, vert_2, weight = int(vert_1), int(vert_2), int(weight)
            
            edges[_] = dict(
                start=vert_1, end=vert_2, weight=weight
            )

        file_in.close()

    print(max_weight(edges))


if __name__ == '__main__':
    main()
