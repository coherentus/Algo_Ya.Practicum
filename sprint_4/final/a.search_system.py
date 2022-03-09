def get_relevant(request, documents):
    answer = list()
    req_words = set(request.split())
    for word in request:

    


def main():
    num_documents = int(input())
    documents_db = list()
    for count in range(num_documents):
        document_in = input().split
        document = dict()
        for word in document_in:
            try:
                document[word] += 1
            except IndexError:
                document[word] = 1
        # порядковый номер
        documents_db[count][0] = count + 1
        # список слов
        documents_db[count][1] = document
    
    num_requests = int(input())
    for count in num_requests:
        result = get_relevant(input(), documents_db)
        print(*result)


if __name__ == '__main__':
    main()
