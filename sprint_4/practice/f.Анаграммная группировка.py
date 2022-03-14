def add_word(words, in_word, index):
    chars = sorted([char for char in in_word])
    tmp = words.get(chars)
    if tmp:
        tmp.append(index)
        words[chars] = tmp
    else:
        words[chars] = [index]


def check_anagram(words):
    pass


def main():
    _ = int(input())
    db_words = dict()
    result = list()
    count = 0
    for word in input().split():
        add_word(db_words, word, count)
        count += 1

    result = check_anagram(db_words)
    for answ in result:
        print(*answ)


if __name__ == '__main__':
    main()
