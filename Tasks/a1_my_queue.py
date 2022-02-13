"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, elem: Any) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        # начало очереди - слева - dequeue
        # конец очереди - справа - enqueue
        self.queue.append(elem)
        print(elem)
        return None

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if no elements.

        :return: dequeued element
        """
        if not self.queue:
            return None
        dequeued_elem = self.queue[0]
        del self.queue[0]
        return dequeued_elem

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """

        print(ind)
        if not self.queue:
            return None
        elif ind > len(self.queue)-1:
            return None
        else:
            value = self.queue[ind]

        return value

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.queue.clear()
        return None
