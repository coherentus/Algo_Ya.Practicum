def func(a_value, x_value, b_value, c_value):
    """Return value of ax^2 + bx + c

    Args:
        a_value (int):
        x_value (int):
        b_value (int):
        c_value (int):
    """
    return a_value * x_value ** 2 + b_value * x_value + c_value


def main():
    a_value, x_value, b_value, c_value = list(map(int, input().split()))
    print(func(a_value, x_value, b_value, c_value))


if __name__ == '__main__':
    main()
