class HashTable:
    size = 100000
    
    def __init__(self):
        self._data = [None for _ in range(self.size)]
 
    def __getitem__(self, key):
        h = self.__get_hash(key)
        return self._data[h]
 
    def __setitem__(self, key, value):
        h = self.__get_hash(key)
        self._data[h] = value
 
    def __get_hash(self, name):
        return name % self.size

def get_res(table, requ):
    """Вернуть результат действия из запроса.
    
    """
    command, *args = requ.split()
    if command == 'put':
        value = args[1]
    key = args[0]

    return table.command(key, value)


def main():
    num_requests = int(input())
    hash_table = HashTable()
    for _ in range(num_requests):
        request = input()
        result = get_res(hash_table, request)
        print(result)

if __name__ == '__main__':
    main()


class OverLenght(Exception):
    """Исключение для ошибок переполнения."""

    def __init__(self, message):
        self.message = message


class ZeroLenght(Exception):
    """Исключение для ошибок извлечения из пустого дека."""

    def __init__(self, message):
        self.message = message


class Deque():
    """Дек - двусторонняя очередь.

    Построен на типе List.
    Конструктор принимает аргумент size - размер дека.
    Имеет методы для добавления и извлечения эл-тов,
    как с головы, так и хвоста.
    Для манипуляций используются индексы эл-тов.
    Изменение размера не предусмотрено.
    В случае ошибок длины дека генерит исключения:
    OverLenght
    ZeroLenght
    """

    def __init__(self, size: int) -> None:
        """Создать экземпляр класса Дек.

        Аргумент:
            size (int): размер структуры в элементах.
        Атрибуты:
        __size - максимальный размер
        __lenght - текущая длина
        __head - индекс для операций с головой дека.
        новую голову писать по индексу (__head - 1),
        текущую читать по индексу __head.
        __tail - индекс для операций с хвостом дека.
        новый писать по индексу __tail,
        текущий хвост читать по индексу (__tail + 1)
        __items - эл-ты дека
        """
        self.__size: int = size
        self.__items: List[Optional[str]] = [None] * size
        self.__lenght: int = 0
        self.__head: int = 0
        self.__tail: int = 0

    def __check_max_lenght(self) -> None:
        """Выбросить ошибку если для заполненного дека вызван push()."""
        if self.__lenght == self.__size:
            raise OverLenght(f'Текущий размер дека = {self.__lenght}'
                             ' Добавление элемента невозможно')

    def __check_zero_lenght(self) -> None:
        """Выбросить ошибку если при нулевой длине вызван pop()."""
        if self.__lenght == 0:
            raise ZeroLenght(f'Текущий размер дека = {self.__lenght}'
                             ' Извлечение элемента невозможно')

    def __calc_idx(self, unclean_idx: int) -> int:
        """Вспомогательный метод для пересчёта индекса.

        Аргументы:
            unclean_idx - индекс + смещение, может выходить за индексы
            начала (0) и конца массива (self.__size - 1)
        Метод возвращает корректное значение для индекса кольцевой структуры
        используя деление по модулю из максимального размера self.__size
        """
        return unclean_idx % self.__size

    def push_back(self, item: str) -> None:
        """Добавить эл-т после хвоста дека.

        Если текущая длина меньше размера:
        По индексу __tail вписать новый эл-т.
        "Увеличить" __tail.
        Увеличить __lenght.
        """
        self.__check_max_lenght()
        self.__items[self.__tail] = item
        self.__tail = self.__calc_idx(self.__tail + 1)
        self.__lenght += 1

    def push_front(self, item: str) -> None:
        """Добавить эл-т перед головой дека.

        Если текущая длина меньше размера:
        "уменьшить" __head, вписать новый эл-т.
        Увеличить __lenght.
        """
        self.__check_max_lenght()
        self.__head = self.__calc_idx(self.__head - 1)
        self.__items[self.__head] = item
        self.__lenght += 1

    def pop_back(self) -> Optional[str]:
        """Снять эл-т с хвоста дека.

        Если текущая длина не ноль:
        "Уменьшить" __tail.
        Взять эл-т по индексу __tail, вписать None.
        Уменьшить длину дека __lenght.
        Вернуть эл-т.
        """
        self.__check_zero_lenght()
        self.__tail = self.__calc_idx(self.__tail - 1)
        res: Optional[str] = self.__items[self.__tail]
        self.__lenght -= 1
        return res

    def pop_front(self) -> Optional[str]:
        """Снять эл-т с головы дека.

        Если текущая длина не ноль:
        Взять эл-т по индексу __head, вписать None.
        "Увеличить" __head.
        Уменьшить длину дека __lenght.
        Вернуть эл-т.
        """
        self.__check_zero_lenght()
        res: Optional[str] = self.__items[self.__head]
        self.__head = self.__calc_idx(self.__head + 1)
        self.__lenght -= 1
        return res
