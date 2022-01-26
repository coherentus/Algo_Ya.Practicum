def parity_compare(num_1, num_2, num_3):
    """Return True if parity of args are same.

    Args:
        num_1 (int):
        num_2 (int):
        num_3 (int):

    Returns:
        boolean:
    """
    if (num_1 % 2 == num_2 % 2 and num_2 % 2 == num_3 % 2):
        return True

def main():
    num_1, num_2, num_3= list(map(int, input().split()))
    if parity_compare(num_1, num_2, num_3):
        print('WIN')
    else:
        print('FAIL')


if __name__ == '__main__':
    main()
