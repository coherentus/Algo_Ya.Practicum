"""
функция heap_add(heap, key):
    index = heap.size + 1
    heap[index] = key
    sift_up(heap, index)

функция sift_up(heap, index):
    если index == 1, то
        завершить работу
    parent_index = index / 2  (целочисленное деление)
    если heap[parent_index] < heap[index], то
        обменять местами heap[parent_index] и heap[index]
        sift_up(heap, parent_index)
"""
"""
функция pop_max(heap):
  result = heap[1]
    heap[1] = heap[heap.size]
  heap.size -= 1
  sift_down(heap, 1)
  верни result

функция sift_down(heap, index):
    left = 2 * index 
    right = 2 * index + 1

        # нет дочерних узлов    
        если heap.size < left, то
            завершить работу
    
        # right <= heap.size проверяет, что есть оба дочерних узла
    если (right <= heap.size) и (heap[left] < heap[right]), то
        index_largest = right
    иначе
        index_largest = left

    если heap[index] < heap[index_largest], то
        обменять местами heap[index] и heap[index_largest]
        sift_down(heap, index_largest) 
"""


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
