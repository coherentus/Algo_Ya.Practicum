# do not declare Node in your submit-file 
class Node: 
    def __init__(self, left=None, right=None, value=0): 
        self.value: int = value 
        self.right = right 
        self.left = left 
################# 
def print_range(node: Node, l: int, r: int):
    result = [None] * 100000
    count = 0

    def go_forward(vertex, left, right):
        
        if l <= vertex.value <= r:
            result[count] = vertex.value
            count += 1

        if not vertex.left is None:
            go_forward(vertex.left, left, right)
        if not vertex.right is None:
            go_forward(vertex.right, left, right)
    
    go_forward(node, l, r)

    for elem in sorted(result):
        if not elem is None:
            print(elem)
    return sorted(result)
