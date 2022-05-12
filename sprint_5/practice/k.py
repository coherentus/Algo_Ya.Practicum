# do not declare Node in your submit-file
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.value = value
        self.right = right
        self.left = left
#################


def print_range(node: Node, l: int, r: int):

    if node is None:
        return

    if node.value < l:
        print_range(node.right, l, r)
    elif node.value > r:
        print_range(node.left, l, r)
    else:
        print_range(node.left, l, r)
        print(node.value)
        print_range(node.right, l, r)
