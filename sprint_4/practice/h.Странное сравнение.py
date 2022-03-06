def check_words(first, second):
    translate = dict()
    second_calc = ''

    for i in range(len(first)):
        key = first[i]
        if key not in translate:
            translate[key] = second[i]
        second_calc += translate[key]

    translate_values = translate.values()
    if len(set(translate_values)) == len(translate):
        if second_calc == second:
            return 'YES'
    return 'NO'


def main():
    first_word = input()
    second_word = input()
    print(check_words(first_word, second_word))


if __name__ == '__main__':
    main()
