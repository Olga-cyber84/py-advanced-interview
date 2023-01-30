# Необходимо реализовать класс Stack со следующими методами:
# is_empty - проверка стека на пустоту. Метод возвращает True или False.
# push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
# pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
# peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
# size - возвращает количество элементов в стеке.
from typing import List


class Stack:
    def __init__(self, _list=[]):
        self._list = _list

    def is_empty(self) -> bool:
        return len(self._list) == 0

    def push(self, item) -> None:
        self._list.insert(0, item)

    def pop(self):
        if self.is_empty():
            pass
        else:
            return self._list.pop(0)

    def peek(self):
        if self.is_empty():
            pass
        else:
            return self._list[0]

    def size(self):
        return len(self._list)


if __name__ == '__main__':
    stack = Stack()
    stack.push(3)
    stack.push(6)
    stack.push(16)
    stack.push(0)
    stack.push(33)
    stack.pop()
    res = stack.peek()
    result = stack.is_empty()
    print('result', res)
    print('res', stack.size())
