def find_neighbors(rows, cols, matrix, target_row, target_col):
    """In matrix find neighbors for target element. Return sorted values.

    Args:
        rows (int): how rows in matrix
        cols (int): how cols in matrix
        matrix (list[list]): matrix
        target_row (int): row idx of target ceil
        target_col (int): col idx of target ceil

    Returns:
        list: neigbors of target
    """
    neighbors = list()

    # If target not in left position, it have left neihbor. Append it.
    if target_col != 0:
        neighbors.append(matrix[target_row][target_col - 1])
    # If target not in right position, it have right neihbor. Append it.
    if target_col != cols - 1:
        neighbors.append(matrix[target_row][target_col + 1])

    # If target not in top position, it have upper neihbor. Append it.
    if target_row != 0:
        neighbors.append(matrix[target_row - 1][target_col])
    # If target not in bottom position, it have lower neihbor. Append it.
    if target_row != rows - 1:
        neighbors.append(matrix[target_row + 1][target_col])

    neighbors.sort()
    return neighbors


def main():
    """
    Input dim-s, matrix itself, coords of desired element. Print neighbors.
    """
    rows = int(input())
    cols = int(input())
    matrix = list()
    for i in range(rows):
        matrix.append(list(map(int, input().split())))
    target_row = int(input())
    target_col = int(input())

    print(*find_neighbors(rows, cols, matrix, target_row, target_col))


if __name__ == '__main__':
    main()
