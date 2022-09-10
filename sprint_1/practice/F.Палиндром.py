def is_palindrom(in_text):
    """Return True if in_text is a palindrom, False if not.

    Args:
        in_text (str): string of numeric, alphabetical and punctuations.
    Returns:
        boolean:
    """
    # выбираем только текстовые символы
    filled_text = ''.join(ch for ch in in_text if ch.isalpha())
    # приводим к нижнему регистру
    lower_text = filled_text.lower()
    # разворачиваем
    revert_text = ''.join(reversed(lower_text))

    if revert_text == lower_text:
        return True
    return False


def main():
    text = input()

    print(is_palindrom(text))


if __name__ == '__main__':
    main()
