def form2num(form: str) -> int:
    """По списочной форме вернуть числовое значение.

    Args:
        form (str): цифры числа разделённые пробелами

    Returns:
        int: само число

    Строка из цифр и пробелов преобразуется в список цифр и разворачивается.
    Начиная с младшего разряда накапливается сумма разрядов:
    - цифра разряда из строки преобразуется в число
    - оно множится на 10 в степени равной номеру разряда
    - младший разряд имеет нулевой номер.
    """
    enum_numbers = enumerate(reversed(form.split()))
    return sum([int(x) * (10 ** y) for y, x in enum_numbers])


def num2form(number: int):
    """Преобразовать число и вернуть списочную форму.

    Args:
        number (int): входное число

    Returns:
        str: цифры, составляющие запись числа через пробел.

    Строка, полученная преобразованием числа используется как
    последовательность символов для join().
    """
    return (' '.join(str(number)))


def main():
    _ = int(input())
    form_x: str = input()
    num_k: int = int(input())
    num_x: int = form2num(form_x)
    print(num2form(num_x + num_k))


if __name__ == '__main__':
    main()
