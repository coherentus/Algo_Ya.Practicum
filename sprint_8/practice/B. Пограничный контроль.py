WRONG_ANSWER = 'FAIL'
RIGHT_ANSWER = 'OK'


def compare_string(str_one, str_two):
    if abs(len(str_one) - len(str_two)) > 1:
        return WRONG_ANSWER

    if len(str_one) > len(str_two):
        str_one, str_two = str_two, str_one

    lhs_pos = 0
    rhs_pos = 0
    one_diff = False
    while lhs_pos < len(str_one) and rhs_pos < len(str_two):
        if str_one[lhs_pos] != str_two[rhs_pos]:
            if one_diff:
                return WRONG_ANSWER
            one_diff = True
            if len(str_one) == len(str_two):
                lhs_pos += 1
        else:
            lhs_pos += 1
        rhs_pos += 1
    return RIGHT_ANSWER


def main():
    """Ввести данные, вызвать обработку, напечатать результат."""
    # ввод данных
    with open('input.txt') as file_in:
        # В первой строке дано имя из паспорта.
        # Во второй строке —- имя из базы.
        # имя человека в базе отличается от имени в паспорте на одну замену,
        # одно удаление или одну вставку символа
        name_doc = file_in.readline().strip()
        name_base = file_in.readline().strip()
        file_in.close()

    print(compare_string(name_doc, name_base))


if __name__ == '__main__':
    main()
