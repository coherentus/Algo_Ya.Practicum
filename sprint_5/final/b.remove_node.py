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
 
def remove(root: Node, key: int) -> Optional[Node]:
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

    # find node
    current_node = root
    is_found: boolean = False
    parent_p: Optional[Node] = None
    while True:
        if current_node.value == key:
            is_found = True
            break
        parent_p = current_node
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
        # Вариант а) Узел - корень.
        if current_node == root:
            return None
        # Вариант б) Узел имеет родителя.
        if parent_p.left == current_node:
            parent_p.left = None
        else:
            parent_p.right = None
        return root

    # Случай 2. Узел имеет потомка(-ов).
    # Вариант а) Нет левого потомка.
    # Замена на самый левый лист в правом поддереве. leftmost
    if parent_p.left is None:
        cur_leftmost_node = parent_p.right
        while True:
            if cur_leftmost_node.left:
                sub_parent = cur_leftmost_node.left
            else:
                sub_value = cur_leftmost_node.value
                sub_parent.right = cur_leftmost_node.right
                current_node.value = sub_value
                






    # Вариант б) Есть левый потомок.
    # Замена на самый правый лист в левом поддереве.

    return root
