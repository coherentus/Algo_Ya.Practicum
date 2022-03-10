def add_words(words_arr, words_input, doc_num):
    """Добавить в базу слов порцию из документа.

    Аргументы:
    words_arr: dict - БД слов.
                      Ключ - слово, значение - список словарей,
                      где ключ - номер документа,
                      значение - кол-во вхождений в документ.

    words_input: list - входящий документ в виде списка всех слов.
    doc_num: int - номер входящего документа.

    Возврат:
    None

    Для каждого слова из запроса:
    - если его ещё нет в БД создаётся "стартовый" эл-т с номером док-та
    - если слово уже есть, создаётся или обновляется существующий эл-т
    """
    for word in words_input:
        if word in words_arr:
            if doc_num in words_arr[word]:
                words_arr[word][doc_num] += 1
            else:
                words_arr[word][doc_num] = 1
        else:
            words_arr[word] = {doc_num: 1}


def get_relevant(request, words_in_docs):
    """Вернуть до 5 самых значимых значений релевантности.

    Аргументы:
    request: list[str] - список слов запроса
    words_in_docs: dict - БД слов с подсчитанными вхождениями

    Возврат:
    list[int]
    Отсортированные по убыванию релевантности и возрастанию номера документа
    значения в кол-ве не более 5-ти.

    При переборе уникальных слов из запроса, в отдельном внутреннем словаре
    накапливаются суммы вхождений этих слов в каждый документ.
    Заполненный словарь преобразуется в двумерный список, список сортируется.
    От среза из первых 5-ти эл-тов берётся вторая колонка и возвращается.
    """
    answer = list()
    words_stat = dict()
    for word in request:
        if word in words_in_docs:
            for doc_num, count_in_doc in words_in_docs[word].items():
                if doc_num in words_stat:
                    words_stat[doc_num] += count_in_doc
                else:
                    words_stat[doc_num] = count_in_doc

    for key, value in words_stat.items():
        answer.append((-value, key))
    answer = sorted(answer)[0:5]
    return [x[1] for x in answer]


def main():
    num_documents = int(input())
    words_db = dict()
    for num_doc in range(1, num_documents + 1):
        document_in = input().split()
        add_words(words_db, document_in, num_doc)

    num_requests = int(input())
    for _ in range(num_requests):
        result = get_relevant(set(input().split()), words_db)
        print(*result)


if __name__ == '__main__':
    main()
