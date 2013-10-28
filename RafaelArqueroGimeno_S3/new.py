class Node:
    __slots__ = ('data', 'link')

    def __init__(self, data = None, link = None):
        self.data = data
        self.link = link

#FIFO
class Queue:
    __slots__ = ('front', 'back')
    
    def __init__(self):
        self.front = self.back = None        

    def isEmpty(self):
        return self.front == None

    def printQ(self):
        print '-' * 8
        
        if(self.isEmpty()):
            print "Empty Queue!"
        else:
            node = self.front
            while node != None:
                print node.data.getTitle()
                node = node.link
        
        print '=' * 8

    def enqueue(self, node):
        node.link = None #security
        if(self.isEmpty()):
            self.back = self.front = node
        else:
            self.back.link = node
            self.back = node
        
    def dequeue(self):
        if self.isEmpty():
            print "Empty Queue! Dequeue is not allowed!"
            return None
        else:
            node = self.front
            self.front = node.link
            if(self.front == None): self.back = self.front
            return node.data

#LIFO                
class Stack:
    __slots__ = ('top')
    
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None
        
    def printStack(self):
        print "-" * 8
        if(self.isEmpty()):
            print "Empty Stack!"
        else:
            node = self.top
            while node != None:
                print node.data.getTitle()
                node = node.link

        print "=" * 8
        
    def push(self, node):
        if self.isEmpty():
            node.link = None
            self.top = node            
        else:
            node.link = self.top
            self.top = node
            
    def pop(self):
        if self.isEmpty():
            print "Empty Stack! Pop is not allowed!"
            return None
        else:
            node = self.top
            self.top = self.top.link
            return node.data
