import copy
import math

from ABB_Rafael_Arquero_Gimeno import ABB


__author__ = "Rafael Arquero Gimeno"


class Hash(object):
    def __init__(self, size=2**10):
        self.size = size
        self.table = [ABB() for i in xrange(self.size)]

    def insert(self, data):
        key = self.function(data.relevance)
        self.table[key].insert(data)

    def isEmpty(self):
        return all(tree.isEmpty() for tree in self.table)

    def function(self, x):
        """The hash function. I observer a logarithmic distribution of data, so i used logarithm as hash function.
        After playing with vars, I found this function, which performs very well"""
        return self.size - 1 + int(math.log(x, 1.01))

    def __copy__(self):
        result = Hash(self.size)
        self.table = [copy.copy(tree) for tree in self.table]
        return result

    def __nonzero__(self):
        return any(tree for tree in self.table)

    def __iter__(self):
        for tree in reversed(self.table):
            for data in tree:
                yield data

    def __str__(self):
        return reduce(lambda x, y: x + str(y) + "\n", self, "")
