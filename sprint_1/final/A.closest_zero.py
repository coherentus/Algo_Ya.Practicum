from typing import List, Optional


def closest_zero(houses: List[str], lenght: int) -> List[int]:
    """Для эл-тов списка найти расстояние до ближайшего 0.

    На входе -
    houses: список строк. Одна из них обязательно == '0'.
    lenght: длина списка.
    На выходе - список целых значений, где 0 позиционно
    соответствует '0' из houses, а остальные == расстоянию
    до ближайшего '0'.
    """
    left_zero: Optional[int] = None
    answer: List[int] = [0] * lenght
    work_houses: enumerate = enumerate(houses)
    steps: int = 0
    for index, value in work_houses:
        if value != '0':  # во входном массиве попался номер дома
            steps += 1
            # пишем нарастающие значения от 1
            answer[index] = steps
        else:  # во входном массиве попался ноль
            if steps:  # если есть шаги - есть промежуток значений
                if left_zero is not None:  # левый ноль уже есть
                    # между индексами left_zero и index
                    # в answer вписаны значения вида "1, 2, 3, ..., N"
                    # длина или (index - left_zero) или steps

                    # счётчик нужных эл-тов
                    # если steps чётный, то берёт половину
                    # если steps нечётный, то берёт до середины невключительно
                    halfed: int = steps // 2
                    left_start = left_zero + 1

                    answer[index - halfed: index] = (
                        answer[left_start: left_start + halfed][::-1]
                    )
                else:
                    # левый ноль не определён, диапазон от начала до '0'
                    # заполнен '1, 2, 3, ..., N'. разворачиваем
                    answer[0: index] = answer[0: index][::-1]
                steps = 0
            # шагов нет, значит повторяется 0
            # обновляем левый ноль
            left_zero = index
    return answer

def main():
    num_count: int = int(input())
    input_numbers: List[str] = [x for x in input().split()]
    results: List[int] = closest_zero(input_numbers, num_count)
    print(*results)


if __name__ == '__main__':
    main()
