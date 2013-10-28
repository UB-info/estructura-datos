import random
from time import time

import parserLastFM
import HEAPInterface
import ABBInterface
import HASHInterface

__author__ = "Rafael Arquero Gimeno"


def benchmarkFunction(function, *args):
    """Returns a tuple containing the result of the given function and the time consumed"""
    start = time()
    tmp = function(*args)
    end = time()
    return tmp, end - start


def benchmarkModule(module):
    """returns a tuple with the average cost of add and search in ms in given module
    :param module:
    """
    costs = {"add": [], "search": []}
    parser = parserLastFM.parser("LastFM_big.dat")
    users = module.emptyType()

    for i in xrange(10):
        users, cost = benchmarkFunction(module.add, users, parser)
        costs["add"].append(cost)

    for i in xrange(10):
        minRandom = random.uniform(0.0, 1.0)
        maxRandom = random.uniform(minRandom, 1.0)
        tmp, cost = benchmarkFunction(module.search, users, minRandom, maxRandom)
        costs["search"].append(cost)

    del users, parser
    return costs


def printRow(row, width=20):
    for cell in row:
        print cell,
        print " " * (width - len(str(cell))),
    print


def printTable(table):
    """

    :type table: dict
    """
    separator = "-" * 80

    # header
    print separator
    headers = table.keys()
    printRow([""] + headers)
    print separator

    # add costs
    for i in xrange(len(table[headers[0]]["add"])):
        row = [table[header]["add"][i] for header in headers]
        row.insert(0, "Add " + str(i + 1))
        printRow(row)
    minRow = [min(table[header]["add"]) for header in headers]
    minRow.insert(0, "Min Add")
    maxRow = [max(table[header]["add"]) for header in headers]
    maxRow.insert(0, "Max Add")
    averageRow = [sum(table[header]["add"]) / float(len(table[header]["add"])) for header in headers]
    averageRow.insert(0, "Average Add")
    print
    printRow(minRow)
    printRow(maxRow)
    printRow(averageRow)
    print separator

    # search costs
    for i in xrange(len(table[headers[0]]["search"])):
        row = [table[header]["search"][i] for header in headers]
        row.insert(0, "Search " + str(i + 1))
        printRow(row)
    minRow = [min(table[header]["search"]) for header in headers]
    minRow.insert(0, "Min Search")
    maxRow = [max(table[header]["search"]) for header in headers]
    maxRow.insert(0, "Max Search")
    averageRow = [sum(table[header]["search"]) / float(len(table[header]["search"])) for header in headers]
    averageRow.insert(0, "Average Search")
    print
    printRow(minRow)
    printRow(maxRow)
    printRow(averageRow)
    print separator


if __name__ == "__main__":
    pattern = 'In {0}, the average time spent in adding is {1:.4}ms and {2:.4}ms in searching.'
    modules = {"Binary Search Tree": ABBInterface, "Heap": HEAPInterface, "Hash": HASHInterface}
    # modules = {"Binary Search Tree": ABBInterface, "Hash": HASHInterface}
    costs = dict()

    print "[!] All time are in seconds"

    for name, module in modules.iteritems():
        print '{0} benchmark started!'.format(name)
        costs[name] = benchmarkModule(module)
        print '{0} benchmark finished!'.format(name)
    print

    printTable(costs)

