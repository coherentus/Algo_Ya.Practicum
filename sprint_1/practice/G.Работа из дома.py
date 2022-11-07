def binary_view(number):
    binary_number = ''
    while True:
        quotient = number // 2
        if number % 2 == 0:
            binary_number = '0' + binary_number
        else:
            binary_number = '1' + binary_number
        if quotient == 0:
            break
        number = quotient
    return binary_number


def main():
    decimal_number = int(input())

    print(binary_view(decimal_number))


if __name__ == '__main__':
    main()
