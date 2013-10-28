import copy
from itertools import cycle, islice

from model import *
import view
import parserLastFM


__author__ = "Rafael Arquero Gimeno"


def add(users, parser):
    """

    :type users: Heap
    :type parser: parser
    """

    for user in islice(parser, 5000):
        users.insert(user)
    return users


def search(source, minimum=0.0, maximum=1.0):
    """

    :type source: Heap
    """
    assert minimum <= maximum

    src_copy = copy.copy(source)
    result = []

    tmp = src_copy.pop()
    while tmp > maximum:
        tmp = src_copy.pop()

    while tmp >= minimum:
        result.append(tmp)
        tmp = src_copy.pop()

    return cycle(result) if result else None  # None if no results


def remove(source, minimum=0.0, maximum=1.0):
    source.pop()
    return source


def useful_info(heap):
    """

    :type heap: Heap
    """
    return "Depth: " + str(heap.depth)


def emptyType():
    return Heap()


if __name__ == "__main__":
    parser = parserLastFM.parser("LastFM_small.dat")
    app = view.MainApp(parser, add, search, remove, useful_info, emptyType())
    app.mainloop()
