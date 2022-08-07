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


def main():
    with open('input.txt') as file_in:
        # кол-во матчей
        num_duels = int(file_in.readline())
        # очки за матчи
        scores = list(map(int, file_in.readline().split()))

        file_in.close()

    print(get_parity(scores))


if __name__ == '__main__':
    main()
