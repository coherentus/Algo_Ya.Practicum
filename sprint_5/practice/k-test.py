# do not declare Node in your submit-file
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.value = value
        self.right = right
        self.left = left
#################


def print_range(node: Node, l: int, r: int):

    def print_forward(node, left, right):
        if node is None:
            return

        if left <= node.value <= right:
            print(node.value)

        if node.right is not None:
            print_forward(node.right, left, right)
        if node.left is not None:
            print_forward(node.left, left, right)

    print_forward(node, l, r)


def main():
    node5 = Node(None, None, 15)
    node4 = Node(None, node5, 11)
    node3 = Node(None, None, 1)
    node2 = Node(node3, None, 3)
    root = Node(node2, node4, 7)
    print_range(root, 6, 14)


if __name__ == '__main__':
    main()
