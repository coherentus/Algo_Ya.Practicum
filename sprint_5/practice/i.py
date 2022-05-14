def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


def answ(num):  # числа каталана
    return int(factorial(2 * num) / (factorial(num) * factorial(num + 1)))


def main():
    n = int(input())
    print(answ(n))


if __name__ == '__main__':
    main()
