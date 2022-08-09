from itertools import compress, product


def get_parity(score_arr):
    # Если сумма нечётна - ответ False
    scores_sum = sum(score_arr)
    if scores_sum % 2:
        return False

    # Полусумма
    scores_sum_half = scores_sum / 2

    score_arr = sorted(score_arr)

    max_score = score_arr[-1]
    if scores_sum_half < max_score:
        return False

    odd_count = 0
    for item in score_arr:
        if item % 2:
            odd_count += 1
    if odd_count % 2:
        return False


def partition_equal_sums_brute_force(numbers):
    if sum(numbers) % 2 == 0: # even sum
        for selectors in product([0, 1], repeat=len(numbers)):
            if sum(compress(numbers, selectors)) == sum(numbers) // 2:
                return True
    return False


def find_split(source):
    n = len(source)
    K = sum(source)
    h_K = K // 2
    # P ← пустая булева таблица размера (K/2 + 1) by (n + 1)
    P = [[False] * (n + 1)] * (K // 2 + 1)
    # инициализируем верхнюю строку (P(0,x)) таблицы P значениями True
    P[0] = [True] * (K // 2 + 1)
    # инициализируем крайний левый столбец (P(x, 0)) таблицы P,
    # за исключением ячейки P(0, 0) значениями False
    
    # для i от 1 до K/2
    for i in range(1, h_K + 1):
        # для j от 1 до n
        for j in range(1, n + 1):
            # если (i-S[j-1]) >= 0
            if (i-source[j-1]) >= 0:
                P[i][j] = (P[i][j-1] or P[i-source[j-1]][j-1])
            else:
                P[i][j] = P[i][j-1]
    return P[h_K][n]



def main():
    with open('input.txt') as file_in:
        # кол-во матчей
        num_duels = int(file_in.readline())
        # очки за матчи
        scores = list(map(int, file_in.readline().split()))

        file_in.close()
    print(find_split(scores))
    #print(partition_equal_sums_brute_force(scores))
    # print(get_parity(scores))


if __name__ == '__main__':
    main()
