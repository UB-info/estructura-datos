__author__ = "Rafael Arquero Gimeno"

from ABB_Rafael_Arquero_Gimeno import ABB


class User:
    def __init__(self, uid, age, gender, country, songs_played, relevance):
        self.__uid = uid
        self.__age = age
        self.__gender = gender
        self.__country = country
        self.__songs_played = songs_played
        self.__most_played = songs_played[0]
        self.__relevance = relevance / 100.0

    def __str__(self):
        # id is elided, is too long!
        return "User: {0}...\nCountry: {1}\nAge: {2} \nGender: {3}\nMost Played: {4}\nRelevance: {5:.2%}\n".format(
            self.__uid[:16], self.__country, self.__age, self.__gender, self.__most_played.name, self.__relevance)

    def __cmp__(self, other):
        return cmp(self.relevance, other.relevance) if isinstance(other, User) else cmp(self.relevance, other)

    @property
    def relevance(self):  # relevance getter
        return self.__relevance


class Artist:
    def __init__(self, *args):
        self.name = args[0]
        #I found corruption in big.dat file. An artist parsed without times (i.e. no "::" to split)
        self.times = 0 if len(args) is 1 else int(args[1])  # 0 if value is not provided

    def __str__(self):
        return self.name + ' ' + str(self.times)

    def __cmp__(self, other):
        return cmp(self.times, other.times)


class Node:
    def __init__(self, data=None):
        self.data = data
        self.link = None


class Queue:  # FIFO
    def __init__(self):
        self.front = self.back = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, data):
        node = Node(data)
        if self.isEmpty():
            self.back = self.front = node
        else:
            self.back.link = node  # make the last point to node
            self.back = node  # now, node is the last

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            node = self.front
            self.front = node.link
            if self.front is None:
                self.back = self.front
            return node.data

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.front.data

    def walker(self, endless=False):
        node = self.front
        while node is not None:
            yield node.data
            node = node.link

        if endless:
            while True:  # infinite loop
                for x in self.walker():
                    yield x

    def insert(self, data):
        self.enqueue(data)

    def __str__(self):
        return reduce(lambda x, y: x + str(y) + "\n", self.walker(), "")


class PQueue(Queue):
    def enqueue(self, data):
        node = Node(data)

        if self.isEmpty():
            self.back = self.front = node
        elif self.back.data >= data:  # lower than the lowest
            #BONUS: this if placed first boost performance when we search and enqueue one more time
            self.back.link = node  # make the last point to node
            self.back = node  # now, node is the last
        elif self.front.data <= data:  # bigger than the biggest
            node.link = self.front  # node points to front
            self.front = node  # node is front
        else:  # somewhere in the middle
            before = self.front  # the element immediate higher that data
            after = self.front.link  # the element immediate lower that data
            while after.data > data:
                #uncoment for traditional but not boost enqueue
                #before, after = after, after.link
                try:  # ULTRA BOOST PERFORMANCE! walking 50 by 50 instead 1 by 1
                    boost = after
                    # equivalent to after.link.link... 50 times
                    for x in xrange(50):
                        boost = boost.link
                    assert boost.data > data
                    before, after = boost, boost.link
                except:
                    before, after = after, after.link

            #now, we've found higher and lower correlated elements
            #then, make sandwich!
            node.link = after
            before.link = node
