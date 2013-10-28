__author__ = "Rafael Arquero Gimeno"

from model import *
import view
import parserLastFM


def add(parser):
    """
    :param parser: File parser
    :return: A Binary Search Tree containing old + parsed values
    """
    return parser.next()


def search(tree, minimum=0.0, maximum=1.0):
    """Returns an iterator that returns values inside the interval in the given tree
    :rtype : generator
    :param tree: Original Tree
    :param minimum: lower bound
    :param maximum: higher bound
    """
    assert 0 <= minimum <= 1
    assert 0 <= maximum <= 1
    assert minimum <= maximum

    # tree is passed by reference, clone is done to safely operate through tree
    result = ABB().clone(tree).deleteLower(minimum).deleteHigher(maximum)

    return None if result.isEmpty() else result.inOrder(endless=True)


def remove(tree, minimum=0.0, maximum=1.0):
    """Returns a tree with with the values of given tree if they are out of given interval"""
    assert 0 <= minimum <= 1
    assert 0 <= maximum <= 1
    assert minimum <= maximum

    lowers, highers = ABB().clone(tree).deleteHigher(minimum), ABB().clone(tree).deleteLower(maximum)

    root = highers.min()  # the lowest of highers, can be the root
    highers.delete(root, wholeNode=True)

    result = ABB().insert(root)
    result.root.left = lowers.root
    result.root.right = highers.root

    return result


def initParser(filename):
    """Returns a parser ready for retrieve users from given file"""
    return parserLastFM.parser(filename, ABB())


if __name__ == "__main__":

    users = ABB()
    parser = initParser('LastFM_small.dat')

    app = view.MainApp(parser, add, search, remove, users)
    app.mainloop()
