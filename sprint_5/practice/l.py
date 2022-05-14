def sift_down(heap: list, idx: int) -> int:
    heap_size = len(heap) - 1

    idx_left = 2 * idx
    idx_right = idx_left + 1

    # нет дочерних узлов
    if heap_size < idx_left:
        return idx

    # right <= heap.size проверяет, что есть оба дочерних узла
    if (idx_right <= heap_size) and (heap[idx_left] < heap[idx_right]):
        index_largest = idx_right
    else:
        index_largest = idx_left

    if heap[idx] < heap[index_largest]:
        heap[idx], heap[index_largest] = heap[index_largest], heap[idx]
        idx = sift_down(heap, index_largest)

    return idx
