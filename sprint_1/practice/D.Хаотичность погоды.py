def chaotic_weather(num_days, thermal_values):
    """Return counter of days with right conditions.

    Args:
        num_days (int): how items in array.
        thermal_values (list of int): thermal per day.

    Returns:
        int: count of days where temp is stronly lowest in days
        before and after each day in array.
        If array have only one day return 1.
    """
    if num_days == 1:
        return 1

    right_count = 0
    # цикл для дней со второго до предпоследнего
    # у них есть предыдущий день и следующий
    for i in range(1, num_days - 1):
        reper = thermal_values[i]
        if (
            reper > thermal_values[i - 1]
            and reper > thermal_values[i + 1]
        ):
            right_count += 1
    # проверка для первого дня
    if thermal_values[0] > thermal_values[1]:
        right_count += 1
    # проверка для последнего дня
    if thermal_values[num_days - 1] > thermal_values[num_days - 2]:
        right_count += 1

    return right_count


def main():
    days_count = int(input())
    days_temp_values = list(map(int, input().split()))

    print(chaotic_weather(days_count, days_temp_values))


if __name__ == '__main__':
    main()
