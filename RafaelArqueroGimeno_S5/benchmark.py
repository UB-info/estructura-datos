__author__ = "Rafael Arquero Gimeno"

import random
from time import time

import PColaInterface
import ABBInterface


def benchmarkFunction(function):
    start = time()
    tmp = function()
    end = time()
    return tmp, end - start


def benchmarkModule(module):
    """returns a tuple with the cost of add and search in ms in given module"""
    start = time()

    for i in xrange(5):  # 10 / 2 = 5
        parser = module.initParser('LastFM_big.dat')
        for j in xrange(2):  # 10000 users / 5000 = 2
            users = module.add(parser)

    middle = time()

    for i in xrange(100):
        minRandom = random.uniform(0.0, 1.0)
        maxRandom = random.uniform(minRandom, 1.0)
        module.search(users, minRandom, maxRandom)

    end = time()

    addCost = 1000.0 * (middle - start) / 10.0
    searchCost = 1000.0 * (end - middle) / 100.0
    return addCost, searchCost  # adding cost and searching cost in ms


if __name__ == '__main__':
    pattern = 'In {0}, the average time spent in adding is {1:.4}ms and {2:.4}ms in searching.'

    abbCosts = benchmarkModule(ABBInterface)
    print pattern.format('Binary Search Tree', *abbCosts)

    pqCosts = benchmarkModule(PColaInterface)
    print pattern.format('Priority Queue', *pqCosts)

    addFactor = abbCosts[0] / pqCosts[0]
    searchFactor = abbCosts[1] / pqCosts[1]
    print
    print 'Conclusion: add is {0:.4} times slower in Priority Queue, but search is {1:.4} times faster.'.format(
        1 / addFactor, searchFactor)
