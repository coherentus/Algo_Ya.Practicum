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
        if not (
            (node.left and node.left.value < node.value)
            and (node.right and node.right.value > node.value)
        )
            return False
        if node.left:
            step(node.left)
        if node.right:
            step(node.right)
    step(root)
    return True
