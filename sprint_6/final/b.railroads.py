SYMB_B = 'B'
SYMB_R = 'R'
RIGHT_RESULT = 'YES'
WRONG_RESULT = 'NO'


def input_line(index, town_arr, in_line):
    """Занести данные в матрицу смежности.

    Args:
        index (int:): номер вершины, для которой переданы данные
        town_arr (list[list:]): матрица вершин, размер больше на 1,
            чтобы номер вершины использовать как индекс, т.е. нулевые
            индексы не используются.
        in_line (str:): строка символов, первый относится к вершине с
            номером index + 1
    Return:
        None. Изменяет переданный аргумент town_arr.

    Граф создаётся направленным.
    Значение 'B' считается прямым направлением, т.е. от меньшего номера
    вершины к большему. Вводятся значением '1' в строку матрицы.
    Значение 'R' - обратным, т.е. от большего номера вершины к меньшему.
    Вводятся значением '1' в столбец матрицы.
    """
    # Карта задана n-1 строкой.
    # В i-й строке описаны дороги из города i в города i+1, i+2, ..., n.
    # В строке записано n - i символов, каждый из которых либо R, либо B.
    # Если j-й символ строки i равен «B»,
    # то из города i в город i + j идет дорога типа «B».
    # Аналогично для типа «R».
    chars_in_line = enumerate(in_line, start=index+1)
    for char_num, char in chars_in_line:
        if char == SYMB_B:
            town_arr[index][char_num] = True
        else:
            town_arr[char_num][index] = True


def check_optimum(towns_arr):
    """Определить 'оптимальность' карты, вернуть результат.

    Args:
        towns_arr list[list[bool:]]: массив вершин,
    Return:
        result str: результат работы алгоритма, 'YES' или 'NO'.

    Граф передан матрицей смежности.
    DFS-обход организуется с покраской вершин. Если будет найден цикл, то
    прекратить работу и вернуть "NO". Иначе вернуть "YES".
    """
    optimum = RIGHT_RESULT  # заготовка ответа
    colors = ['white' for _ in range(len(towns_arr))]
    stack = []
    # цикл MainDFS():
    for i in range(1, len(towns_arr)):
        # Перебираем варианты стартовых вершин, пока они существуют.
        if colors[i] == 'white':
            start_vert = i
            # Вершина посещена, но ещё не обработана.
            colors[start_vert] = 'gray'
            cur_vert = towns_arr[start_vert]
            # [Union(None, True),...] True в положении idx означает
            # наличие ребра из текущей вершины в вершину с номером idx
            for idx in range(1, len(towns_arr)):
                if cur_vert[idx]:
                    if colors[idx] == 'white':
                        stack.append(idx)

            while stack:
                fromm = stack.pop()
                if colors[fromm] == 'white':
                    colors[fromm] = 'gray'
                    cur_vert = towns_arr[fromm]
                    # [Union(None, True),...] True в положении idx означает
                    # наличие ребра из текущей вершины в вершину с номером idx
                    for idx in range(1, len(towns_arr)):
                        if cur_vert[idx]:
                            if colors[idx] == 'white':
                                stack.append(idx)
                            elif colors[idx] == 'gray':
                                optimum = WRONG_RESULT
                                break
                            """elif colors[idx] == 'gray':
                                # Серую вершину мы могли получить из стека
                                # только на обратном пути. Следовательно,
                                # её следует перекрасить в чёрный.
                                colors[idx] = 'black'"""
                else:
                    optimum = WRONG_RESULT
                    break

    """функция DFS(start_vertex):
        stack = Stack()
        stack.push(start_vertex)
        пока stack не пуст:
            # Получаем из стека очередную вершину.
            # Это может быть как новая вершина, так и уже посещённая однажды.
            v = stack.pop()
            если color[v] == white:
                # Красим вершину в серый. И сразу кладём её обратно в стек:
                # это позволит алгоритму позднее вспомнить обратный путь по графу.
                color[v] = gray
                stack.push(v)
                # Теперь добавляем в стек все непосещённые соседние вершины,
                # вместо вызова рекурсии
                для каждого исходящего ребра (v,w):
                    возьмём вершину w
                    если color[w] == white:
                        stack.push(w)
            иначе, если color[v] == gray:
                # Серую вершину мы могли получить из стека только на обратном пути.
                # Следовательно, её следует перекрасить в чёрный.
                color[v] = black"""
    return optimum


def main():
    """Ввести данные, вызвать обработку, напечатать результат.

    """
    # ввод данных
    with open('input.txt') as file_in:
        # кол-во городов
        num_towns = int(file_in.readline())
        # матрица смежности
        towns = [
            [None for _ in range(num_towns + 1)]
            for __ in range(num_towns + 1)
        ]

        # считывание и обработка дорог
        for town_count in range(1, num_towns):
            input_line(town_count, towns, file_in.readline().strip())
        file_in.close()

    print(check_optimum(towns))


if __name__ == '__main__':
    main()
