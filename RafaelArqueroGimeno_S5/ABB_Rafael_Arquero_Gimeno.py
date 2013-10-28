__author__ = "Rafael Arquero Gimeno"


class Node():
    def __init__(self):
        self.data = []
        self.left = None
        self.right = None

    def clear(self):
        """Empty Node"""
        self.data = []
        self.left = None
        self.right = None

    def clearData(self):
        """Empty stored values"""
        self.data = []

    def append(self, data):
        """Appends given value"""
        self.data.append(data)
        return self  # allow method chaining

    def delete(self, data):
        """Deletes the given value from Node"""
        self.data.remove(data)

    def clone(self, other):
        """Makes self clone of another Node

        :type other: Node
        :param other: Original Node to clone
        :rtype : Node (allow method chaining)
        """
        self.data = other.data  # TODO [:]
        self.left = Node().clone(other.left) if other.hasLeftChild() else None
        self.right = Node().clone(other.right) if other.hasRightChild() else None
        return self

    def min(self):
        return self.left.min() if self.hasLeftChild() else self.key()

    def max(self):
        return self.right.max() if self.hasRightChild() else self.key()

    def isEmpty(self):
        return not bool(self.data)

    def key(self):
        return None if self.isEmpty() else self.data[0]

    def hasLeftChild(self):
        """Query if the node has left child

        :rtype: bool
        """
        return self.left is not None

    def hasRightChild(self):
        """Query if the node has right child

        :rtype: bool
        """
        return self.right is not None

    def __cmp__(self, other):
        return cmp(self.key(), other.key()) if isinstance(other, Node) else cmp(self.key(), other)

    def __str__(self):
        return reduce(lambda x, y: x + str(y) + "\n", self.data, "")


class ABB():
    def __init__(self):
        self.root = Node()

    def clone(self, other):
        """Makes self clone of another ABB

        :param other: Original ABB to clone
        :rtype : ABB
        """
        self.root.clone(other.root)
        return self

    def clear(self):
        """Empty the tree"""
        self.root.clear()

    def insert(self, data):
        """Insert a value in tree

        :param data: value to be inserted
        :return: self to allow method chaining
        """
        if self.isEmpty():
            self.root.append(data)
            return self

        parent, current = self._lookup(data)
        if current is None:  # data equivalent node not found!
            setattr(parent, "right" if parent < data else "left", Node().append(data))
        else:  # equivalent node found!
            current.append(data)
        return self

    def delete(self, data, wholeNode=False):
        """Deletes the given Node or Value if it is contained, Therefore do nothing

        :type data: Node or ValueType (e.g. User)
        :type wholeNode: bool
        :param data: The node or value to delete
        :param wholeNode: if whole matched node should be deleted or only the matched value
        """
        parent, current = self._lookup(data)
        if current is not None:  # data was found
            current.clearData() if wholeNode else current.delete(data)
            if current.isEmpty():  # we have deleted the last element from current node!
                if current.hasLeftChild() and current.hasRightChild():  # 2 children
                    newData = current.right.min()
                    current.clearData()
                    current.append(newData)
                    self.delete(newData)
                elif current.hasLeftChild():  # only left child
                    current.clone(current.left)
                elif current.hasRightChild():  # only right child
                    current.clone(current.right)
                else:  # no children
                    if parent is None:
                        parent = self.root
                    setattr(parent, "right" if parent < data else "left", None)

    def deleteLower(self, threshold, current=None, parent=None):
        """Deletes all values below threshold

        :param threshold: All values below that will be deleted
        :param current: The current inspected node (default root)
        :param parent: The parent of current node
        :return: self, allows method chaining
        """
        if current is None:
            if self.isEmpty():
                return self  # break
            else:
                current = self.root

        if current > threshold:
            if current.hasLeftChild():
                self.deleteLower(threshold, current.left, current)
        elif current < threshold:
            if current.hasRightChild():
                self.deleteLower(threshold, current.clone(current.right), parent)
            else:
                if parent is None:
                    self.clear()  # restart root
                else:
                    parent.left = None  # restart current
        else:  # equals
            current.left = None

        return self

    def deleteHigher(self, threshold, current=None, parent=None):
        """Deletes all values above threshold

        :param threshold: All values above that will be deleted
        :param current: The current inspected current (default root)
        :param parent: The parent of current node
        :return: self, allows method chaining
        """
        if current is None:
            if self.isEmpty():
                return self  # break
            else:
                current = self.root

        if current < threshold:
            if current.hasRightChild():
                self.deleteHigher(threshold, current.right, current)
        elif current > threshold:
            if current.hasLeftChild():
                self.deleteHigher(threshold, current.clone(current.left), parent)
            else:
                if parent is None:
                    self.clear()  # restart root
                else:
                    parent.right = None  # restart current
        else:  # equals
            current.right = None

        return self

    def inOrder(self, current=None, endless=False):
        """Creates a generator that walks through the tree in ascending order

        :param current: The current node
        :param endless: If this should never stop
        """
        if current is None:  # first call
            current = self.root

        if current.hasLeftChild():
            for x in self.inOrder(current.left):
                yield x
        for x in current.data:
            yield x
        if current.hasRightChild():
            for x in self.inOrder(current.right):
                yield x

        if endless and current is self.root:
            while True:  # endless loop
                for x in self.inOrder():
                    yield x

    def _lookup(self, data):
        """Internal method. Finds the given value and return the node where it IS or where it SHOULD BE (i.e. None) and
        also his parent node."""
        parent, current = None, self.root
        while current is not None:
            if current < data:  # data should be in right
                parent, current = current, current.right
            elif current > data:  # data should be in left
                parent, current = current, current.left
            else:  # equals
                return parent, current
        return parent, current

    def min(self):
        """Returns the minimum value of the tree"""
        return self.root.min()

    def max(self):
        """Returns the maximum value of the tree"""
        return self.root.max()

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.root.isEmpty()

    def __str__(self):
        return reduce(lambda x, y: x + str(y) + "\n", self.inOrder(), "")