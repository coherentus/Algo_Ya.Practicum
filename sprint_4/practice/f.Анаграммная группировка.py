def add_word(words, in_word, index):
    chars = sorted([char for char in in_word])
    key = ''.join(chars)
    tmp = words.get(key)
    if tmp:
        tmp.append(index)
        words[key] = tmp
    else:
        words[key] = [index]


def check_anagram(words):
    result = list()
    for word in words.values():
        result.append(word)
    return sorted(result)


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
