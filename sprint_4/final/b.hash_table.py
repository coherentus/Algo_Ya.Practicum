from typing import Callable, Dict, List, Optional

HASH_TABLE_SIZE = 100000
OPERATIONS_TABLE: Dict[str, str] = {
    'put': 'setitem',
    'get': 'getitem',
    'delete': 'delitem',
}


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class HashTable:
    """Хеш-таблица. Реализация с ограниченным функционалом.

    Методы:
    - put key value —– добавление пары ключ-значение.
    Если ключ уже есть, то обновить значение.
    - get key –— получение значения по ключу.
    Если ключа нет, то вернуть «None». Иначе вернуть найденное значение.
    - delete key –— удаление ключа.
    Если ключа нет, то вернуть «None». Иначе вернуть найденное значение
    и удалить ключ.
    Число хранимых в таблице ключей не превосходит 10^5.
    Разрешение коллизий с помощью метода цепочек или с помощью открытой адресации.
    Все операции выполняются за O(1) в среднем.
    Рехеширование и масштабирование хеш-таблицы не предусмотрено.
    Ключи и значения —– целые числа.
    """
    def __init__(self, size: int) -> None:
        self.__size: int = size
        self.__items: List[Optional[int]] = [None] * size

    def getitem(self, key: str) -> Optional[int]:
        """Вернуть значение по ключу.

        Args:
            key (int): Запрашиваемый ключ.

        Returns:
            Optional[int]: Значение, если есть, или None.
        Методом __get_hash получить индекс в массиве данных.
        В эл-те массива определить, есть ли уже значение по ключу.
        Вернуть результат.
        """
        h = self.__get_hash(key)
        node = self.__items[h]
        #if not node:
        #    return None
        while node:
            if node.value[0] == key:
                return node.value[1]
            node = node.next

    def setitem(self, key: str, value: str) -> None:
        """Записать значение по ключу.

        Args:
            key (int): Запрашиваемый ключ.
            value (int): Переданное значение.
        Методом __get_hash получить индекс в массиве данных.
        В эл-те массива определить, есть ли уже значение по ключу.
        Если есть - обновить, иначе - создать.
        """
        h = self.__get_hash(key)
        node = self.__items[h]
        if not node:
            self.__items[h] = Node()
            self.__items[h].value[0] = key
            self.__items[h].value[1] = value
            return None
        while node.next:
            if node.value[0] == key:
                node.value[1] = value
                return None
            node = node.next
        node.next = Node()
        node.next.value[0] = key
        node.next.value[1] = value
        return None

    def delitem(self, key: str) -> Optional[int]:
        """Удалить значение по ключу.

        Args:
            key (int): Запрашиваемый ключ.

        Returns:
            Optional[int]: Если есть, то значение, или None.
        Методом __get_hash получить индекс в массиве данных.
        В эл-те массива определить, есть ли уже значение по ключу.
        В переменной для возврата сохранить значение или None.
        Удалить значение и ключ. Вернуть ответ.
        """
        h = self.__get_hash(key)
        node = self.__items[h]
        if not node:
            return None
        prev_node = None
        while node:
            if node.value[0] == key:
                value = node.value[1]
                if prev_node:
                    prev_node.next = node.next
                else:
                    self.__items[h] = node.next
                return value
            node = node.next
        return None

    def __get_hash(self, key: str):
        return int(key) % self.__size


def get_res(table, requ):
    """Вернуть результат действия из запроса."""
    command, *args = requ.split()
    func = getattr(table, OPERATIONS_TABLE[command])
    return func(*args)


def main():
    hash_table = HashTable(HASH_TABLE_SIZE)
    num_requests = int(input())
    for _ in range(num_requests):
        request = input()
        result = get_res(hash_table, request)
        print(result)


if __name__ == '__main__':
    main()
