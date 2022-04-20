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

    # крайние случаи
    # исходное дерево пусто
    if root is None:
        return None
    # искомый ключ в корне и нет потомков
    if ((root.value == key) and (root.left is None and root.right is None)):
        return None

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
    if sub_parent.left is None and sub_parent.right is None:
        current_node.left = None
        return root
    
    # поиск враво до None
    sub_node = sub_parent.right
    while True:
        if sub_node.right is None:  # узел для обмена найден
            current_node.value = sub_node.value
            sub_parent.right = sub_node.left
            return root
        sub_parent = sub_parent.right
        sub_node = sub_node.right

