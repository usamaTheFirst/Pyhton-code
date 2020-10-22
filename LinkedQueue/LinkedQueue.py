"""
Author : Usama Fayyaz
email : usamafiaz1453@gmail.com
Date : 22/10?2020
"""



class LinkedQueue:
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, elem):
        new_node = self._Node(elem, None)
        if self.is_empty():
            self._head = new_node

        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1


if __name__ == "__main__":
    ins = LinkedQueue()
    for i in range(10):
        ins.enqueue(i)
    for i in range(10):
        a=ins.dequeue()
        print(a)