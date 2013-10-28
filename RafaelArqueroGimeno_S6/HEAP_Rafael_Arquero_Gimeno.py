import copy
import random

__author__ = "Rafael Arquero Gimeno"


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    @property
    def depth(self):
        if self:
            left_depth = self.left.depth if self.left else 0
            right_depth = self.right.depth if self.right else 0
            return 1 + max(left_depth, right_depth)
        else:
            return 0

    def __copy__(self):
        result = Node()
        result.data = self.data
        if self.left:
            result.left = copy.copy(self.left)
        if self.right:
            result.right = copy.copy(self.right)
        return result

    def __nonzero__(self):
        """Returns false if the Node is empty, therefore returns True"""
        return self.data is not None

    def __cmp__(self, other):
        return cmp(self.data, other.data) if isinstance(other, Node) else cmp(self.data, other)


class Heap(object):
    def __init__(self):
        self.root = Node()

    @staticmethod
    def strategy(a, b):
        return a >= b  # max-heap strategy by default

    def insert(self, data):
        if self:  # not empty
            parent, current = None, self.root
            tmp = data
            while current is not None:
                if not Heap.strategy(current.data, tmp):  # wrong order
                    current.data, tmp = tmp, current.data  # swap them
                parent, current = current, current.left if random.random() > 0.5 else current.right  # TODO criteria
            if parent.right:
                parent.left = Node(data)
            else:
                parent.right = Node(data)
        else:
            self.root.data = data

    def dequeue(self):
        if self:  # not empty
            current = self.root

            while current is not None:
                if current.right and current.left:
                    if Heap.strategy(current.left, current.right):
                        current.data = current.left.data
                        current = current.left
                    else:
                        current.data = current.right.data
                        current = current.right
                elif current.left:
                    current.right = current.left.right
                    current.left = current.left.left
                    current = None
                elif current.right:
                    current.left = current.right.left
                    current.right = current.right.right
                    current = None
                else:  # no children
                    current.data = None
                    current = None

    def pop(self):
        if self:
            tmp = self.root.data
            self.dequeue()
            return tmp
        else:
            return None

    @property
    def depth(self):
        return self.root.depth

    def __copy__(self):
        result = Heap()
        result.root = copy.copy(self.root)
        return result

    def __nonzero__(self):
        """Returns false if the Heap is empty, therefore return True"""
        return self.root.__nonzero__()

    def __iter__(self, current=None):
        if current is None:  # first call
            current = self.root

        if self:
            yield current.data
            if current.left:
                for x in self.__iter__(current.left):
                    yield x
            if current.right:
                for x in self.__iter__(current.right):
                    yield x

    def __str__(self):
        return reduce(lambda x, y: x + str(y) + "\n", self, "")
