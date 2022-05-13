# https://contest.yandex.ru/contest/24810/run-report/68349532/
# Задача Б. Написать функцию для удаления ключа бинарного дерева.
# На входе - корень дерева и ключ. На выходе - корень изменённого
# дерева. Создавать  новые вершины нельзя.
#
# -- ПРИНЦИП РАБОТЫ --
# Работа функции заключается в двух этапах:
# - первый - это поиск узла с заданным ключом, если ключ не найден,
# возвращается исходное дерево.
# - второй - собственно удаление.
#
# Удаление имеет несколько вариантов:
# - удаляемый узел - лист (не имеет потомков).
# Удаление заключается записью в родительском узле None.
#
# - удаляемый узел имеет одного потомка.
# Удаление заключается в записи ссылки на этого потомка в родительский узел.
#
# - удаляемый узел имеет двух потомков(левое и правое поддерево).
# В этом варианте ищется самый правый узел в левом поддереве.
# Если это лист, то его значение переносится в "удаляемый" узел, а сам лист
# удаляется.
# Если самый правый узел содержит имеет потомка(как следствие, левого),
# то значение найденного правого узла переносится в "удаляемый" узел,
# а левого потомка этого правого узла усыновляет родительский узел правого
# узла в качестве правого потомка.
#
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# Теория и механизмы работы с бинарным деревом наглядно рассмотрены по ссылке
# https://practicum.yandex.ru/learn/algorithms/courses/7f101a83-9539-4599-b6e8-8645c3f31fad/sprints/21363/topics/e7dbf42a-fd5a-434b-990d-9cfe0e3a10c8/lessons/03eb9b46-4c74-43b4-8d00-a125aeed47bf/
# В реализации добавлены проверки существования объектов перед обращением
# к ним.
#
# -- ОЦЕНКА СЛОЖНОСТИ --
#
# Если эл-т для удаления - лист, то сложность удаления не превышает O(h)
# в худшем случае, где h - высота дерева.
# Для других случаев сложность также составит не более O(h) в худшем случае,
# так как алгоритм проходит от корня дерева через удаляемый эл-т до кандидата
# на перестановку один раз, в худшем случае этот путь может равняться высоте
# дерева. Пространственная сложность никаким образом не зависит ни от кол-ва
# эл-ов дерева ни от его высоты, следовательно, составляет O(1).
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.value = value
        self.right = right
        self.left = left


def remove(root, key: int):
    """Найти и удалить вершину с заданным ключом.

    Args:
        root (Node): Корень дерева.
        key (int): Искомый ключ.

    Returns:
        Node: Корень результирующего дерева.

    Алгоритм работы.
    Ключ ищется один раз, так как уникален по условию.
    Если ключ - лист, то у его родителя устанавливается None.
    Если ключ имеет одного потомка, то этот потомок вписывается
    у родителя вместо ключа.
    Если у ключа два потомка, то ищется самый правый узел в левом
    поддереве, он вписывается вместо удаляемого.
    """
    # крайние случаи
    # исходное дерево пусто
    if root is None:
        return None

    # искомый ключ в корне
    if root.value == key:
        # и нет потомков
        if root.left is None and root.right is None:
            return None

        # потомок один
        if (root.left is not None) and (root.right is None):
            root = root.left
            return root
        if (root.left is None) and (root.right is not None):
            root = root.right
            return root
        # если дошли сюда, то потомков два
        # удаление будет осуществляться заменой на самый правый узел
        # левого поддерева
        parent_p: Node = root.left  # предполагаемая вершина левого поддерева

        # вариант 1. Вершина левого поддерева не имеет правого потомка.
        # - Эта вершина на место правого потомка усыновляет правое поддерево
        # удаляемого узла(root-а).
        # - за root принять эту вершину левого поддерева.
        if parent_p.right is None:
            parent_p.right = root.right
            root = parent_p
            return root

        # вариант 2. Вершина левого поддерева имеет правого потомка.
        # Ведётся поиск самого правого узла(листа).
        while True:
            current_p = parent_p.right
            if current_p.right is None:  # найден самый правый
                # - на место правого потомка усыновить правое поддерево
                # удаляемого узла(root-а)
                # - в родительском узле самого правого усыновить левого
                # потомка самого правого(включая None)
                # - на место левого потомка самого правого усыновить
                # левое поддерево удаляемого узла (root-а)
                # - принять за новый root бывший самый правый из левого
                # поддерева
                current_p.right = root.right
                parent_p.right = current_p.left
                current_p.left = root.left
                root = current_p
                return root
            parent_p = current_p

    # find node
    # current_node - текущий узел, проверяемый на ключ
    # parent_d - его родитель
    is_found: bool = False

    # инициализация parent_d и current_node перед циклом поиска
    if root.value > key:
        current_node = root.left
    else:
        current_node = root.right
    parent_d: Node = root

    while True:
        if current_node.value == key:
            is_found = True
            break
        parent_d = current_node
        if current_node.value > key:
            if current_node.left is None:
                break
            current_node = current_node.left
        else:
            if current_node.right is None:
                break
            current_node = current_node.right

    # Узел не найден.
    if not is_found:
        return root

    # Узел найден.
    # current_node - найденный узел, подлежащий удалению.
    # parent_d - его родитель.
    # Случай 1. Узел это лист.
    if current_node.right is None and current_node.left is None:
        if parent_d.left == current_node:
            parent_d.left = None
        else:
            parent_d.right = None
        return root

    # Случай 2. Узел имеет одного потомка.

    # нет левого
    # в родителя передвинуть правого потомка
    if current_node.left is None:
        if parent_d.left == current_node:
            parent_d.left = current_node.right
        elif parent_d.right == current_node:
            parent_d.right = current_node.right
        return root
    # нет правого
    # в родителя передвинуть левого потомка
    if current_node.right is None:
        if parent_d.left == current_node:
            parent_d.left = current_node.left
        elif parent_d.right == current_node:
            parent_d.right = current_node.left
        return root

    # Случай 3. Удаляемый узел имеет 2-х потомков.
    # Заменить удаляемый самым правым из левого поддерева.
    # на этот момент:
    # current_node - узел для удаления
    # parent_d - его родитель.

    # вершина левого поддерева
    sub_parent: Node = current_node.left

    # если у этого узла нет правого потомка, то:
    # - в этом узле(sub_parent) усыновить правое поддерево удаляемого
    # узла sub_parent.right <- current_node.right
    # - в родителе удаляемого узла(parent_d) усыновить этот
    # бывший лист sub_parent
    if sub_parent.right is None:
        sub_parent.right = current_node.right

        # найти сторону(лево/право) у родителя удаляемого узла
        if parent_d.left == current_node:
            parent_d.left = sub_parent
        else:
            parent_d.right = sub_parent
        return root

    # поиск враво до None в цикле
    # sub_node станет узлом для замещения удаляемого узла
    # sub_parent - его родителем
    sub_node: Node = sub_parent.right
    while True:
        if sub_node.right is None:  # узел для обмена найден
            # - родитель узла для обмена усыновляет левого потомка
            # этого узла, в том числе и None. sub_node отвязан от
            # дерева, а его потомков можно перезаписывать.
            # - sub_node усыновляет левого и правого потомков узла,
            # подлежащего удалению(current_node).
            # - родитель удаляемого узла усыновляет sub_node.
            sub_parent.right = sub_node.left
            sub_node.left = current_node.left
            sub_node.right = current_node.right

            if parent_d.left == current_node:
                parent_d.left = sub_node
            else:
                parent_d.right = sub_node
            return root

        sub_parent = sub_parent.right
        sub_node = sub_node.right
