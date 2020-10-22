"""
Author : Usama Fayyaz
email : usamafiaz1453@gmail.com
Date : 22/10?2020
"""


class LinkedSTack:
    # nested class for a node in stack
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, element):
        self._head = self._Node(element, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")

        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")

        value = self._head._element
        self._head = self._head._next
        self._size -= 1
        return value

    def check_stack_values(self):
        temp = self._head
        while temp is not None:
            print(temp._element)
            temp = temp._next


if __name__ == "__main__":
    instance = LinkedSTack()
    for i in range(10):
        instance.push(i)
    a = instance.top()
    print(a)
    instance.check_stack_values()
