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
def sift_up(heap: list, idx: int) -> int:
    if idx == 1:
        return 1
    parent_index = idx // 2
    if heap[parent_index] < heap[idx]:
        heap[parent_index], heap[idx] = heap[idx], heap[parent_index]
        idx = sift_up(heap, parent_index)
    
    return idx

"""            
def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1
"""