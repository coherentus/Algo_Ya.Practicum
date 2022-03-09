def get_relevant(request, words_in_docs):
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
        answer.append((value, key))
    answer = sorted(answer, reverse=True)[0:5]
    answer = [x[1] for x in answer]
    # print(answer[0:5])
        # {num_doc: count}
    return answer


def main():
    num_documents = int(input())
    # db format key - word, values - {number_of_doc: count_in_doc}
    words_db = dict()
    for num_doc in range(1, num_documents + 1):
        document_in = input().split()
        for word in document_in:
            if word in words_db:
                if num_doc in words_db[word]:
                    words_db[word][num_doc] += 1
                else:
                    words_db[word][num_doc] = 1
            else:
                words_db[word] = {num_doc: 1}

    num_requests = int(input())
    for req_count in range(num_requests):
        result = get_relevant(input().split(), words_db)
        print(*result)


if __name__ == '__main__':
    main()
