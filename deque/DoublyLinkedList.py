class _DoublyLinkedBased:

    class _Node:
        __slots__ = "_element", "_prev", "_next"

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def insert_between(self, element, pred, succes):
        newest = self._Node(element, pred, succes)
        pred._next = newest
        succes._prev = newest
        self._size += 1

    def _delete_node(self, node):
        node._prev._next = node._next
        node._next._prev = node._prev
        self._size -= 1
        return node._element


class LinkedDeque(_DoublyLinkedBased):
    class Empty(Exception):
        pass
    def first(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self._trailer._prev._element


    def insert_first(self,e):
        self.insert_between(e,self._header,self._header._next)


    def insert_last(self,e):
        self.insert_between(e,self._trailer._prev,self._trailer)


    def delete_first(self):
        if self.is_empty():
            raise self.Empty("Deque is empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self._delete_node(self._trailer._prev)


if __name__ == "__main__":
    a =LinkedDeque()
    a.insert_first(3)
    a.insert_first(3)
    a.insert_first(3)
    a.insert_first(1)

    
    while a.last():
       b= a.delete_last()
       print(b)
