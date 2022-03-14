def add_word(words, in_word, index):
    chars = sorted([char for char in in_word])
    tmp = words.get(chars)
    if tmp:
        tmp.append(index)
        words[chars] = tmp
    else:
        words[chars] = [index]

def check_anagram(words):
    
    

def main():
    count_words = int(input())
    db_words = dict()
    result = list()
    count = 0
    for word in input().split():
        add_word(db_words, word, count)
        count += 1

    result + check_anagram(db_words):

    
    
    
    if count_nums:
        input_arr = [None] * count_nums
        idx = 0
        for in_num in input().split():
            input_arr[idx] = int(in_num)
            idx += 1
        answer = find_sums(input_arr, needed_sum)
        print(len(answer))
        for answ in answer:
            print(*answ)
    else:
        print('0')


if __name__ == '__main__':
    main()