from queue import PriorityQueue


def find_max_cost(heaps_arr, full_weight):
    # отсортировать кучи по максим. стоимости c * m
    tmp_quene = PriorityQueue()
    for heap in heaps_arr:
        tmp_quene.put((-(heap[0] * heap[1]), heap))

    exp_weight = 0
    exp_cost = 0
    while exp_weight < full_weight and not tmp_quene.empty():
        cur_heap = tmp_quene.get()
        if cur_heap[1][1] < full_weight - exp_weight:
            exp_weight += cur_heap[1][1]
            exp_cost += -cur_heap[0]
    return exp_cost


def main():
    """Ввести данные, вызвать обработку, напечатать результат."""
    # ввод данных
    with open('input.txt') as file_in:
        # грузоподъёмность рюкзака Гоши (0 ≤ M ≤ 108)
        max_weight = int(file_in.readline())
        # количество куч с золотым песком — целое число n (1 ≤ n ≤ 10**5)
        num_heaps = int(file_in.readline())

        heaps = [None for _ in range(num_heaps)]

        # считывание куч
        # c и m, записанными через пробел (1 ≤ c ≤ 10**7, 1 ≤ m ≤ 10**8)
        # c - стоимость, m - вес
        for heap_count in range(num_heaps):
            price, weight = file_in.readline().split()
            heaps[heap_count] = (int(price), int(weight))
        file_in.close()

    print(find_max_cost(heaps, max_weight))


if __name__ == '__main__':
    main()
