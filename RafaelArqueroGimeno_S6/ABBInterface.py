import copy
from itertools import cycle, islice

from model import *
import view
import parserLastFM


__author__ = "Rafael Arquero Gimeno"


def add(users, parser):
    """

    :type users: ABB
    :param parser: File parser
    :return: A Binary Search Tree containing old + parsed values
    """
    for user in islice(parser, 5000):
        users.insert(user)
    return users


def search(source, minimum=0.0, maximum=1.0):
    """Returns an iterator that returns values inside the interval in the given tree
    :rtype : generator
    :param source: Original Tree
    :param minimum: lower bound
    :param maximum: higher bound
    """
    assert minimum <= maximum

    # tree is passed by reference, copy is done to safely operate through tree
    result = copy.copy(source)
    result.deleteLower(minimum).deleteHigher(maximum)

    return cycle(result) if result else None


def remove(source, minimum=0.0, maximum=1.0):
    """Returns a tree with with the values of given source if they are out of given interval
    :type source: ABB
    """
    assert minimum <= maximum

    lowers, highers = copy.copy(source), copy.copy(source)
    lowers.deleteHigher(minimum)
    highers.deleteLower(maximum)

    root = highers.min  # the lowest of highers, can be the root
    highers.delete(root, wholeNode=True)

    result = ABB().insert(root)
    result.root.left = lowers.root
    result.root.right = highers.root

    return result


def useful_info(tree):
    """Returns a string with useful info about the given ABB

    :type tree: ABB
    """
    return "Depth: " + str(tree.depth)


def emptyType():
    return ABB()


if __name__ == "__main__":
    parser = parserLastFM.parser("LastFM_small.dat")
    app = view.MainApp(parser, add, search, remove, useful_info, emptyType())
    app.mainloop()
