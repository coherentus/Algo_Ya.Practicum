from queue import PriorityQueue


ERROR_MESSAGE = 'Oops! I did it again'


def edge_input(vert_arr, edge_line: str):
    """По условию добавить данные в список вершин.

    Args:
        vert_arr (list(dict(int:key: int:value))): массив вершин,
            индекс это номер вершины, словарь - инцидентные рёбра,
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
        # граф ненаправленный, поэтому данные ребра добавляются в обе вершины
        # если вершина уже упоминалась, то это кратное ребро, обновить
        # значение веса, если он больше

        # ин-фа для первой о второй
        cur_vert: dict = vert_arr[vert_1]
        if cur_vert.setdefault(vert_2, weight) < weight:
            cur_vert[vert_2] = weight

        # ин-фа для второй о первой
        cur_vert = vert_arr[vert_2]
        if cur_vert.setdefault(vert_1, weight) < weight:
            cur_vert[vert_1] = weight


def max_weight(vertexs_full):
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
    max_tree_weights: int = 0   # Веса рёбер, составляющие MaxST.

    vert_in_tree = list()  # Множество вершин, уже добавленных в остов.
    vert_in_graph = list()  # Множество вершин, ещё не добавленных в остов.

    # Промежуточное хранилище для рёбер, потенциально могущих войти в остов.
    # Добавляются в виде (вес, [нач.вершина, кон.вершина]) приоритет - вес.
    potent_edges = PriorityQueue()

    # В графе есть все вершины от 1 до кол-ва вершин
    for vert_num in range(1, len(vertexs_full)):
        vert_in_graph.append(vert_num)

    # Из множества вершин графа берём первую.
    v = 1
    vert_in_tree.append(v)
    vert_in_graph.remove(v)

    # рёбра этой вершины добавить в кандидаты на остов.
    # Добавляем все рёбра, которые инцидентны v
    # vertexs[v] - словарь смежных с v вершин {вершина: вес}
    for end_vert, weight in vertexs_full[v].items():
        # пишем в очередь с приоритетом на минимум
        potent_edges.put(
            (-weight, (v, end_vert))
        )

    while (not potent_edges.empty()) and vert_in_graph:
        # взять ребро с максимальным весом
        # (вес, (вершина, вершина))
        # первая вершина уже в остове, вторую проверить
        # ребро учитывается, если вторая вершина не в остове
        cur_edge = potent_edges.get()
        secnd_vert = cur_edge[1][1]
        if secnd_vert not in vert_in_tree:
            max_tree_weights -= cur_edge[0]
            vert_in_tree.append(secnd_vert)
            vert_in_graph.remove(secnd_vert)
            for end_vert, weight in vertexs_full[secnd_vert].items():
                # пишем в очередь с приоритетом на минимум
                potent_edges.put(
                    (-weight, (secnd_vert, end_vert))
                )

    if vert_in_graph:
        return ERROR_MESSAGE
    else:
        return max_tree_weights


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

        # для графа из одной вершины
        if num_vert == 1:
            print('0')
            """file_in.close()
            exit()"""
            return

        # если есть признак несвязности графа
        if num_vert - num_edg > 1:
            print(ERROR_MESSAGE)
            """file_in.close()
            exit()"""
            return

        vertexs = [dict() for _ in range(num_vert + 1)]
        # считывание и обработка рёбер
        for _ in range(num_edg):
            edge_input(vertexs, file_in.readline())

        file_in.close()

    print(max_weight(vertexs))


if __name__ == '__main__':
    main()
