from model import *
import view
import parserLastFM
from copy import copy

def add(users, parser):
    try:
        users.merge(parser.next())
        #print "Got", len(users), "users"#debug
    finally:
        return users

def search(users, low = 0.0, high = 1.0):
    '''Filter an users priorityqueue by relevance user attribute (between high and low)'''
    assert 0 <= low <= 1
    assert 0 <= high <= 1
    assert low <= high    

    result      = emptyType()
    userscopy   = copy(users)#users is pased by reference, this is to safely operate through users
    value       = userscopy.dequeue()#actual value

    while value is not None and value.relevance() > high:#higher than max
        value = userscopy.dequeue()#next value
    
    while value is not None and value.relevance() >= low:#higher than min (and lower than max) => matches
        result.enqueue(value)#append to results
        value = userscopy.dequeue()#next value
        
    return result

def get_next(queue):
    '''Returns an element of the given queue'''
    return queue.dequeue()#param is pased by ref, original is also dequeued!

def initparser(filename):    
    return parserLastFM.parser(filename, PQueue)

def emptyType():
    '''returns an empty instance of class PQueue'''
    return PQueue()

if __name__ == '__main__':
    parser = initparser('LastFM_small.dat')    
    app = view.MainApp(parser, add, search, get_next, emptyType())
    app.mainloop()
