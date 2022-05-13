class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root1: Node, root2: Node) -> bool:

    if (root1 is None) and (root2 is None):
        return True

    if (root1 is None) or (root2 is None):
        return False

    if root1.value == root2.value:
        return (
            solution(root1.left, root2.left)
            and solution(root1.right, root2.right)
                )
    else:
        return False
