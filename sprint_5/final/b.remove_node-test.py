"""
Дано бинарное дерево поиска, в котором хранятся ключи.
Ключи — уникальные целые числа. Найдите вершину с заданным ключом
и удалите её из дерева так, чтобы дерево осталось корректным
бинарным деревом поиска. Если ключа в дереве нет,
то изменять дерево не надо.
На вход вашей функции подаётся корень дерева и ключ, который надо удалить.
Функция должна вернуть корень изменённого дерева. Сложность удаления
узла должна составлять O(h), где h –— высота дерева.
Создавать новые вершины (вдруг очень захочется) нельзя.
"""
# do not declare Node in your submit-file 
from typing import Optional
from xmlrpc.client import boolean


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
    Обход LMR.
    Если ключ - лист, то у его родителя устанавливается None.
    
    """
    from typing import Optional

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
        if (not root.left is None) and (root.right is None):
            root = root.left
            return root
        if (root.left is None) and (not root.right is None):
            root = root.right
            return root

    # find node
    current_node = root
    is_found: boolean = False
    parent_d: Optional[Node] = None
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

    # вершина поддерева
    sub_parent = current_node.left
    # если левый узел - лист, его просто удалить
    # его значение вписать в найденный узел
    if sub_parent.left is None and sub_parent.right is None:
        current_node.value = current_node.left.value
        current_node.left = None
        return root
    
    # поиск враво до None
    sub_node = sub_parent.right
    if sub_node is None:  # узла вправо нет
            current_node.value = sub_parent.value
            current_node.left = sub_parent.left
            return root
    while True:
        if sub_node.right is None:  # узел для обмена найден
            current_node.value = sub_node.value
            sub_parent.right = sub_node.left
            return root
        sub_parent = sub_parent.right
        sub_node = sub_node.right
"""
7
1 4 2 3
2 2 4 5
3 6 6 7
4 1 -1 -1
5 3 -1 -1
6 5 -1 -1
7 7 -1 -1
6
"""
def make_tree():
    node7 = Node(None, None, 7)
    node6 = Node(None, None, 5)
    node5 = Node(None, None, 3)
    node4 = Node(None, None, 1)
    node3 = Node(node6, node7, 6)
    node2 = Node(node4, node5, 2)
    root = Node(node2, node3, 4)
    """node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)"""
    return root

def main():
    
    print(remove(make_tree(), 6))


if __name__ == '__main__':
    main()
