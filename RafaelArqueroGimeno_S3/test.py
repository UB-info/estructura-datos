from new import *

def stack(movieList):
    ## THIS IS TO TEST YOUR CODE - STACK
    newStack = Stack()
    newStack.printStack()

    newNode = Node(movieList[0])
    newStack.push(newNode)
    newStack.printStack()

    newStack.push(Node(movieList[1]))
    newStack.printStack()

    newStack.push(Node(movieList[2]))
    newStack.printStack()

    m1 = newStack.pop()
    newStack.printStack()

    m2 = newStack.pop()
    newStack.printStack()

    m3 = newStack.pop()
    newStack.printStack()

    m4 = newStack.pop()
    newStack.printStack()

    print m1.getTitle()
    print m2.getTitle()
    print m3.getTitle()
    ##print m4.GetTitle()  GUESS WHAT HAPPENS...

def queue(movieList):
    ## THIS IS TO TEST YOUR CODE - QUEUE
    newQ = Queue()
    newQ.printQ()
    
    newNode = Node(movieList[0])
    newQ.enqueue(newNode)
    newQ.printQ()
    
    newQ.enqueue(Node(movieList[1]))
    newQ.printQ()
    
    newQ.enqueue(Node(movieList[2]))
    newQ.printQ()
    
    m1 = newQ.dequeue()
    newQ.printQ()
    
    m2 = newQ.dequeue()
    newQ.printQ()
    
    m3 = newQ.dequeue()
    newQ.printQ()
    
    m4 = newQ.dequeue()
    newQ.printQ()
    
    print m1.getTitle()
    print m2.getTitle()
    print m3.getTitle()
    ##print m4.GetTitle()  GUESS WHAT HAPPENS...
