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
    # nodes_values = list()
    def step(node):
        if (node.left is None) and (node.right is None):
            return
        left_ok, right_ok = True, True
        if node.left and (node.left.value >= node.value):
            left_ok = False
        if node.right and (node.right.value <= node.value):
            right_ok = False

        if (left_ok is False) or (right_ok is False):
            return False

        if node.left:
            if step(node.left) is False:
                return False
        if node.right:
            if step(node.right) is False:
                return False
    if step(root) is False:
        return False
    return True
