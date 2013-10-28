__author__ = "Rafael Arquero Gimeno"

from copy import copy

from model import *
import view
import parserLastFM


def add(parser):
    return parser.next()


def search(queue, minimum=0.0, maximum=1.0):
    """Filter a priority queue by relevance user attribute (between maximum and minimum)"""
    assert 0 <= minimum <= 1
    assert 0 <= maximum <= 1
    assert minimum <= maximum

    result = PQueue()
    queueCopy = copy(queue)  # queue is passed by reference, this is to safely operate through queue

    value = queueCopy.dequeue()  # actual value
    while value is not None and value.relevance > maximum:  # higher than max
        value = queueCopy.dequeue()  # next value

    while value is not None and value.relevance >= minimum:  # higher than min (and lower than max) => matches
        result.enqueue(value)  # append to results
        value = queueCopy.dequeue()  # next value

    return None if result.isEmpty() else result.walker(True)


def remove(queue, minimum=0.0, maximum=1.0):
    assert 0 <= minimum <= 1
    assert 0 <= maximum <= 1
    assert minimum <= maximum

    result = PQueue()
    queueCopy = copy(queue)

    value = queueCopy.dequeue()
    while value is not None and value > maximum:
        result.enqueue(value)  # append to results
        value = queueCopy.dequeue()  # next value

    while value is not None and value.relevance >= minimum:  # higher than min (and lower than max) => remove
        value = queueCopy.dequeue()  # next value

    while value is not None:  # below minimum until bottom...
        result.enqueue(value)  # append to results
        value = queueCopy.dequeue()  # next value

    return result


def initParser(filename):
    return parserLastFM.parser(filename, PQueue())

if __name__ == "__main__":
    users = PQueue()
    parser = initParser('LastFM_small.dat')
    app = view.MainApp(parser, add, search, remove, users)
    app.mainloop()
