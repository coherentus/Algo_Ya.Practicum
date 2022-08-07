def get_levenshtein(string_one, string_two):
    pass


def main():
    with open('input.txt') as file_in:
        first_string = file_in.readline()
        second_string = file_in.readline()
        file_in.close()

    print(get_levenshtein(first_string, second_string))


if __name__ == '__main__':
    main()
