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
def sift_down(heap: list, idx: int) -> int:
    heap_size = len(heap) - 1
     
    cld_idx_l = idx * 2
    if cld_idx_l > heap_size:
        cld_idx_l = None
    cld_idx_r = cld_idx_l + 1
    if cld_idx_r > heap_size:
        cld_idx_r = None

    # потомков нет
    if (cld_idx_l is None) and (cld_idx_r is None):
        return idx
    
    # один потомок, только левый.
    if cld_idx_r is None:
        heap[idx], heap[cld_idx_l] = heap[cld_idx_l], heap[idx]
        return cld_idx_l
    
    # оба потомка есть
    # меньше обоих детей
    # менять с большим
    if (heap[idx] < heap[cld_idx_l]) and (heap[idx] < heap[cld_idx_r]):
        if heap[cld_idx_l] < heap[cld_idx_r]:
            heap[idx], heap[cld_idx_r] = heap[cld_idx_r], heap[idx]
            idx = sift_down(heap, cld_idx_r)
        else:
            heap[idx], heap[cld_idx_l] = heap[cld_idx_l], heap[idx]
            idx = sift_down(heap, cld_idx_l)
    
    return idx

"""            
def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1
"""