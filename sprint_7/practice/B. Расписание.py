def get_max_lessons(less_arr):
    result = []
    prev = (0, 0)
    for lesson in less_arr:
        if lesson[1] >= prev[0]:
            prev = lesson
            result.append(prev)
    return result


def main():
    with open('input.txt') as file_in:
        # кол-во дней
        num_lessons = file_in.readline()
        num_lessons = int(num_lessons)
        times_less = [None] * num_lessons
        for idx in range(num_lessons):
            start, stop = file_in.readline().split()
            start_dot = start.find('.')
            if start_dot == -1:
                start_time = int(start) * 60
            else:
                start_h, start_m = start.split('.')
                start_time = int(start_h) * 60 + int(start_m)
            if '.' in stop:
                stop_h, stop_m = stop.split('.')
                stop_time = int(stop_h) * 60 + int(stop_m)
            else:
                stop_time = int(stop) * 60
            times_less[idx] = (stop_time, start_time)

        file_in.close()
        times_less = sorted(times_less)

    schedule = get_max_lessons(times_less)
    print(len(schedule))
    for lesson in schedule:
        stop, start = lesson
        stop_m = stop % 60
        if stop_m:
            stop = str(stop // 60) + '.' + str(stop_m)
        else:
            stop = stop // 60
        start_m = start % 60
        if start_m:
            start = str(start // 60) + '.' + str(start_m)
        else:
            start = start // 60

        print(start, stop)


if __name__ == '__main__':
    main()
