from queue import PriorityQueue


ERROR_MESSAGE = 'Oops! I did it again'

def edge_input(vert_arr, edge_line: str):
    """По условию добавить данные в список вершин.

    Args:
        vert_arr (list(dict(int:key: int:value))): массив вершин,
            индекс это номер вершины, словарь - инцидентное ребро,
            ключ - номер смежной вершины, а значение - вес.
        edge_line (str): строка ввода, содержит три значения.
    
    В графе могут быть петли и кратные рёбра. Для поиска остовного
    дерева в них нет надобности. Петли просто игнорятся, а из
    кратных рёбер остаётся с наибольшим весом.
    
    Фунция изменяет данные в переданном массиве, ничего не возвращает.
    """
    # вершины, соединяемые ребром и вес этого ребра
    vert_1, vert_2, weight = edge_line.split()
    vert_1, vert_2, weight = int(vert_1), int(vert_2), int(weight)

    if not vert_1 == vert_2:  # отброс петель
        # граф ненаправленный, поэтому от ребра добавляются обе вершины
        # если вершина уже упоминалась, то это кратное ребро, обновить
        # значение веса, если он больше
        
        # ин-фа для первой о второй
        cur_vert: dict = vert_arr[vert_1]
        
        """if vert_2 in cur_vert:
            cur_val = cur_vert[vert_2]
            if weight > cur_val:
                cur_vert[vert_2] = weight
        else:
            cur_vert[vert_2] = weight"""
        
        if cur_vert.setdefault(vert_2, weight) < weight:
            cur_vert[vert_2] = weight
        
        # ин-фа для второй о первой
        cur_vert: dict = vert_arr[vert_2]
        if cur_vert.setdefault(vert_1, weight) < weight:
            cur_vert[vert_1] = weight


def extract_max(edges):
    """Найти ребро с максимальным весом, удалить из edges и вернуть.

    Args:
        edges ([
            {v_1: NN, v_2: MM, weight: XX}
            ]
        ): Набор рёбер графа, где ключи 'v_1' и 'v_2' это вершины,
        а 'weight' это вес ребра. Значения всех ключей - int(целые числа)

    Returns:
        {v_1: NN, v_2: MM, weight: XX}: найденное ребро с максимальным весом
    
    Проверка на корректность аргумента не производится. Аргумент может быть
    изменён функцией.
    """
    max_e = edges[0]
    for edge in edges:
        if max_e['weight'] < edge['weight']:
            max_e = edge
    edges.remove(max_e)
    return max_e



def max_weight(vertexs_full, how_edges):
    """Найти максимальное остовное дерево. Вернуть его вес.

    Args:
        vertexs_full [
            {vert_number: weight, ...},
        ]
        Индекс эл-та это номер вершины, к которой относится словарь.
        Ключ словаря это номер смежной вершины, значение - вес.
        Размер списка на единицу больше кол-ва вершин для удобства
        нумерации, т.е. нулевой эл-т не используется.
        Все ключи и значения типа int(целые числа).
        how_edges (:int) Кол-во рёбер в графе.
    
    Return:
        Суммарный вес максимального остовного дерева графа,
        если оно существует, или сообщение об ошибке.
    
    Остовное дерево ищется по алгоритму Прима.
    Берётся первая вершина. В набор потенциальных рёбер добавляются
    все её рёбра. Вершина добавляется в дерево, из просматриваемых удаляется.
    Из набора рёбер выбирается ребро максимального веса, одна вершина ко-
    торого уже в остове, а вторая ещё нет. Оно добавляется в остов и удаляется
    из набора. Другая вершина этого ребра добавляется в набор и удаляется из
    рассматриваемых.
    Если список рассматриваемых вершин не пуст, то с этой вершиной новый цикл
    поиска ребра и след. вершины. Если ребро найти не удаётся,
    то граф несвязный, выдать ошибку.
    """
        #
        # Вершины not_added стоит хранить в таком контейнере,
        # чтобы проверка (end in not_added) выполнялась эффективно.
        #
        # Для этого подойдёт, например, хеш-таблица.
        # Также в некоторых языках программирования имеется контейнер set.
        # edges += graph.edges.filter(start == v, end in not_added)
    
    
    max_tree_weghts = list()   # Веса рёбер, составляющие MST.

    vert_in_tree = set()  # Множество вершин, уже добавленных в остов.
    vert_in_graph = set() # Множество вершины, ещё не добавленных в остов. 
    
    # Промежуточное хранилище для рёбер, потенциально могущих войти в остов.
    # Добавляются в виде (вес, [нач.вершина, кон.вершина]) приоритет - вес.
    potent_edges = PriorityQueue(maxsize=how_edges)
    
    # В графе есть все вершины от 1 до кол-ва вершин
    for vert_num in range(1, len(vertexs_full)):
        vert_in_graph.add(vert_num)

    # Из множества вершин графа берём первую.
    v = vert_in_graph[0]  # 1 другими словами
    vert_in_tree.add(v)
    vert_in_graph.remove(v)
    
    # рёбра этой вершины добавить в кандидаты на остов.
    # Добавляем все рёбра, которые инцидентны v
    # vertexs[v] - словарь смежных с v вершин {вершина: вес}
    for end_vert, weight in vertexs[v].items():
        # пишем в очередь с приоритетом на минимум
        potent_edges.put(
            (-weight, [v, end_vert])
        )
    
    """, но их конец ещё не в остове."""
    if not potent_edges.empty():
        cur_edge = potent_edges.get()
    else:
        return ERROR_MESSAGE
    
    next_vert = cur_edge[1][1]
    
    
    пока vert_in_graph не пуст и potent_edges не пуст:
        # Подразумеваем, что extract_minimum извлекает минимальное ребро 
        # из массива рёбер и больше данного ребра в массива не будет.
        e = extract_minimum(edges)
        если e.end in not_added, то:
        minimum_spanning_tree += e
        add_vertex(e.end)

    если vert_in_graph не пуст, то 
        верни ошибку "Исходный граф несвязный"
    иначе
        верни minimum_spanning_tree 


def main():
    """Ввести данные, вызвать обработку, напечатать результат.
    
    Граф вводится в структуру вида:
    vertexs = [
        {vert_number: weight, ...},
    ]
    Индекс эл-та это номер вершины, к которой относится словарь.
    Ключ словаря это номер смежной вершины, значение - вес.
    Размер списка на единицу больше кол-ва вершин для удобства
    нумерации, т.е. нулевой эл-т не используется.
    """
    # ввод данных
    with open('input.txt') as file_in:
        # кол-во вершин и рёбер
        num_vert, num_edg = file_in.readline().split()
        num_vert, num_edg = int(num_vert), int(num_edg)
        if num_vert - num_edg > 1:
            print(ERROR_MESSAGE)
            return
        
        vertexs = [dict() for _ in range(num_vert + 1)]
        # считывание и обработка рёбер
        for _ in range(num_edg):
            edge_input(vertexs, file_in.readline())

        file_in.close()

    print(max_weight(vertexs, num_edg))


if __name__ == '__main__':
    main()
