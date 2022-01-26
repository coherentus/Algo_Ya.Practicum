def find_longest_word(text):
    """Return longest word in text.

    Args:
        text (list of str):

    Returns:
        str: first longest word
        int: lenght of this word
    """
    max_len = 0
    max_word = ''
    for word in text:
        len_word = len(word)
        if len_word > max_len:
            max_len = len_word
            max_word = word
    return max_word, max_len

def main():
    _ = int(input())
    in_text = list(map(str, input().split()))
    
    longest_word, len_word = find_longest_word(in_text)
    
    print(longest_word)
    print(len_word)


if __name__ == '__main__':
    main()
