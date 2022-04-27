# do not declare Node in your submit-file
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.value = value
        self.right = right
        self.left = left
#################
def print_range(node: Node, l: int, r: int):
    arr = [None] * 10000
    COUNT = 0

    def print_forward(node, left, right, arr):
        if node is None:
            return

        if left <= node.value <= right:
            arr[COUNT] = node.value
            COUNT = COUNT + 1

        if not node.left is None:
            print_forward(node.left, left, right, arr)
        if not node.right is None:
            print_forward(node.right, left, right, arr)

    print_forward(node, l, r, arr)

    for num in sorted(arr[0:COUNT]):
        print(num)
