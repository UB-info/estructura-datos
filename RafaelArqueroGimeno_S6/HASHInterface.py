import copy
from itertools import cycle, islice

from model import *
import view
import parserLastFM


__author__ = "Rafael Arquero Gimeno"


def add(users, parser):
    """


    :type users: Hash
    """
    for user in islice(parser, 5000):
        users.insert(user)
    return users


def search(source, minimum=0.0, maximum=1.0):
    """

    :type source: Hash
    """
    assert minimum <= maximum

    result = Hash(source.size)

    for key in xrange(source.size):
        source_tree = source.table[key]

        if source_tree:  # not empty
            min_node, max_node = source_tree.min, source_tree.max

            if minimum <= min_node and max_node <= maximum:
                result.table[key] = copy.copy(source_tree)
            elif min_node <= minimum <= max_node:
                result.table[key] = copy.copy(source_tree).deleteLower(minimum)
            elif min_node <= maximum <= max_node:
                result.table[key] = copy.copy(source_tree).deleteHigher(maximum)

    return cycle(result) if result else None


def useful_info(source):
    return ""


def emptyType():
    return Hash()


if __name__ == "__main__":
    parser = parserLastFM.parser("LastFM_small.dat")
    app = view.MainApp(parser, add, search, None, useful_info, emptyType())
    app.mainloop()
