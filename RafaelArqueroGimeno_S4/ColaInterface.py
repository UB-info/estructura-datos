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
    '''Filter an users queue by relevance user attribute (between high and low)'''
    assert 0 <= low <= 1
    assert 0 <= high <= 1
    assert low <= high    

    result      = emptyType()
    userscopy   = copy(users)#users is pased by reference, this is to safely operate through users
    value       = userscopy.dequeue()
    while value is not None:#iterate over users until we reach the last user
        if low <= value.relevance() <= high:#matches
            result.enqueue(value)
        value = userscopy.dequeue()#next value       
    return result

def get_next(queue):
    return queue.dequeue()

def initparser(filename):    
    return parserLastFM.parser(filename, Queue)

def emptyType():
    '''returns an empty instance of class Queue'''
    return Queue()

if __name__ == '__main__':
    parser = initparser('LastFM_small.dat')
    app = view.MainApp(parser, add, search, get_next, emptyType())
    app.mainloop()
