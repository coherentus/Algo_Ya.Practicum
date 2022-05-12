class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


def solution(root):
    #  Your code
    #  “ヽ(´▽｀)ノ”
    nodes_values = list()

    def step(node, arr):
        arr.append(node.value)
        if (node.right is None) and (node.left is None):
            return
        if node.left:
            step(node.left, arr)
        if node.right:
            step(node.right, arr)
    step(root, nodes_values)
    return max(nodes_values)


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3
