class User:
    def __init__(self, uid, age, gender, country, songs_played):        
        self.__uid          = uid       
        self.__age          = age       
        self.__gender       = gender       
        self.__country      = country      
        self.__songs_played = songs_played

        #print max(songs_played) == songs_played[0]#debug

        self.__most_played  = songs_played[0]#assume that are already sorted (I check it before)
        #if we dont asume that artists are already sorted...
        #self.__most_played  = max(songs_played)

        sum_times           = reduce(lambda x, y: x + y.times, songs_played, 0)#sumatory of times of all artists
        coef                = 1.0 * self.__most_played.times / sum_times#percentage of the best respect total
        
        self.__relevance    = coef

    def __str__(self):
        out = ""
        out += "User: " + self.__uid[:16] + "..." + "\n"#id is ellided, is too long!
        out += "Country: " + self.__country + "\n"
        out += "Age: " + str(self.__age) + "\n"
        out += "Gender: " + str(self.__gender) + "\n"
        out += "Most Played: " + self.__most_played.name + "\n"
        out += "Relevance: " + '{0:.2%}'.format(self.__relevance)#percentage formating
        return out

    def __cmp__(self, other):
        return cmp(self.__relevance, other.relevance())

    def relevance(self):
        #relevance getter
        return self.__relevance

class Artist:
    __slots__ = ('name', 'times')

    def __init__(self, *args):
            self.name  = args[0]
            #I found corruption in big.dat file. An artist parsed without times (i.e. no "::" to split)
            if len(args) > 1:#times is provided
                self.times = int(args[1])
            else:#times is not provided
                self.times = 0   
            
    def __str__(self):
        return self.name + ' ' +  str(self.times)

    def __cmp__(self, other):
        return cmp(self.times, other.times)

class Node:
    __slots__ = ('data', 'link')

    def __init__(self, data = None, link = None):
        self.data = data
        self.link = link

#FIFO
class Queue:
    __slots__ = ('front', 'back')
    
    def __init__(self):
        self._len = 0
        self.front = self.back = None        

    def isEmpty(self):
        return self.front == None

    def enqueue(self, data):
        node = Node(data, None)
        if(self.isEmpty()):
            self.back = self.front = node
        else:
            self.back.link = node#make the last point to node
            self.back = node#now, node is the last

        self._len += 1
        
    def dequeue(self):
        if self.isEmpty():            
            return None
        else:
            self._len -= 1
            node = self.front
            self.front = node.link
            if(self.front == None): self.back = self.front
            return node.data

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.front.data

    def merge(self, other):
        if self.isEmpty():
            self.front = other.front
            self.back  = other.back
        else:            
            self.back.link = other.front
            self.back = other.back

        self._len += len(other)

    def __len__(self):
        return self._len

class PQueue(Queue):
    __slots__ = ('front', 'back')

    def merge(self, other):
        self._len += len(other)

        if self.isEmpty():#this is empty, then this should be equals to other
            self.front = other.front
            self.back = other.back
        else:
            #first check, the front should be the biggest
            if self.front.data < other.front.data:#front is not the biggest
                self.front, other.front = other.front, self.front#interchange
            a = self.front
            b = other.front
            while a.link is not None:#
                #print a.data.relevance(), b.data.relevance()
                #remember: a > b is maintaned
                if b.data > a.link.data:
                    c = a.link#tmp var, b1 = a2
                    a.link = b#a1 points to b1
                    b = c
                else:#a2 >= b1
                    a = a.link#a point to next, normal order
            #print a.link, b#debug
            a.link = b#trivial, since a > b and there is no a's next            
    
    def enqueue(self, data):  
        node = Node(data, None)        
        self._len += 1
        
        if(self.isEmpty()):
            self.back = self.front = node
        elif self.back.data >= data:#lower than the lowest
            #BONUS: this if placed first boost performance when we search and enqueue one more time
            self.back.link = node#make the last point to node
            self.back = node#now, node is the last
        elif self.front.data <= data:#bigger than the biggest
            node.link = self.front#node points to front
            self.front = node#node is front
        else:#somewhere in the middle
            before = self.front#the element inmediate higher that data 
            after = self.front.link#the element inmediate lower that data            
            while after.data > data:                
                before, after = after, after.link
            #now, we've found higher and lower correlated elements
            #then, make sandwich!
            node.link = after
            before.link = node
        
