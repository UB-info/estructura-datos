import ColaInterface
import PColaInterface
import random
from time import time

def benchmark(module):
    '''returns a tuple with the cost of add and search in ms in given module'''
    parser = module.initparser('LastFM_big.dat')
    users  = module.emptyType()
    
    start  = time()
    for i in xrange(10):
            users = module.add(users, parser)
    middle      = time()
    for i in xrange(100):
        lowrandom  = random.uniform(0.0, 1.0)
        highrandom = random.uniform(lowrandom, 1.0)
        #print lowrandom, highrandom#debug
        module.search(users, lowrandom, highrandom)
    end         = time()

    adding      = 1000.0 * (middle - start) / 10.0
    searching   = 1000.0 * (end - middle) / 100.0
    return adding, searching#adding cost and searching cost in ms

if __name__ == '__main__':
    pattern = 'In {0}, the average time spent in adding is {1:.4}ms and {2:.4}ms in searching.'
    
    qcosts  = benchmark(ColaInterface)
    print pattern.format('Queue', *qcosts)
    
    pqcosts = benchmark(PColaInterface)
    print pattern.format('PriorityQueue', *pqcosts)

    addfactor       = qcosts[0] / pqcosts[0]
    searchfactor    = qcosts[1] / pqcosts[1]
    print 'Conclusion: add in PriorityQueue is {0:.4} times slower but search is {1:.4} times faster.'.format(1/addfactor, searchfactor)
