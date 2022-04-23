# do not declare Node in your submit-file 
class Node: 
    def __init__(self, left=None, right=None, value=0): 
        self.value = value 
        self.right = right 
        self.left = left 
################# 
def print_range(node: Node, l: int, r: int):
    result = []

    def go_forward(vertex, left, right, res):
        print(vertex.value)
        if l <= vertex.value <= r:
            result.append(vertex.value)

        if not vertex.left is None:
            go_forward(vertex.left, left, right, res)
        if not vertex.right is None:
            go_forward(vertex.right, left, right, res)
    
    go_forward(node, l, r, result)

    for elem in sorted(result):
        print(elem)
    return sorted(result)

5
1 7 2 4
2 3 3 -1
3 1 -1 -1
4 11 -1 5
5 15 -1 -1
6
14