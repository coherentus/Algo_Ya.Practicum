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
        left_ok, right_ok = False, False
        if node.left:
            left_ok = node.left.value < node.value
        else:
            left_ok = True
            print('l ', left_ok)
        if node.right:
            right_ok = node.value < node.right.value
        else:
            right_ok = True
            print('r ', right_ok)
        print('l and r ', not (left_ok and right_ok))
        if not left_ok or not right_ok:
            return False

        """if not (
            (node.left and (node.left.value < node.value))
            and (node.right and (node.right.value > node.value))
        ):
            return False"""
        if node.left:
            step(node.left)
        if node.right:
            step(node.right)
    step(root)
    return True
