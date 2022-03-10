ASCII = {
    'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71,
    'H': 72, 'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78,
    'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85,
    'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90,
    'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103,
    'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110,
    'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117,
    'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122,
}


def get_hash(line, base, modul):
    if len(line) == 1:
        return (ASCII[line[0]] % modul)
    if len(line) == 0:
        return 0

    n = len(line) - 1
    base = base % modul

    result = ASCII[line[n]] % modul
    degree = 1
    for i in range(n - 1, -1, -1):
        degree = (degree * base) % modul
        result += (ASCII[line[i]] * degree)
    return (result % modul)


def main():
    base = 1000
    module = 123987123
    # input_line = input()
    input_line = ''
    out_mass = list()
    for c_1 in 'abcdefghijklmnopqrstuvwxyz':
        for c_2 in 'abcdefghijklmnopqrstuvwxyz':
            for c_3 in 'abcdefghijklmnopqrstuvwxyz':
                for c_4 in 'abcdefghijklmnopqrstuvwxyz':
                    for c_5 in 'abcdefghijklmnopqrstuvwxyz':
                        input_line = c_1+c_2+c_3+c_4+c_5
                        outer = get_hash(input_line, base, module)
                        out_mass.append(outer)
                        # print(outer)
    if not len(set(out_mass)) == len(out_mass):
        print('есть совпадения', len(set(out_mass)), len(out_mass))
    """cand_1 = out_mass[0]
    for i in range(1, len(out_mass)):
        if cand_1 == out_mass[i]:
            print('found ', i)"""

    #print(get_hash(input_line, base, module))


if __name__ == '__main__':
    main()
"""
24283805 bbbb
15179789 aaab
15180788 aaba
15204788 aaza
61462107 abaa



"""