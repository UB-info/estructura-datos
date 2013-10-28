import copy

__author__ = "Rafael Arquero Gimeno"


class Node(object):
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

    @property
    def key(self):
        return self.data[0] if self else None

    @property
    def leftmost(self):
        return self.left.leftmost if self.left else self.key

    @property
    def rightmost(self):
        return self.right.rightmost if self.right else self.key

    @property
    def depth(self):
        if self:
            left_depth = self.left.depth if self.left else 0
            right_depth = self.right.depth if self.right else 0
            return 1 + max(left_depth, right_depth)
        else:
            return 0

    def __copy__(self):
        """Returns a copy of self

        :rtype : Node
        """
        result = Node()
        result.data = copy.copy(self.data)
        if self.left:
            result.left = copy.copy(self.left)
        if self.right:
            result.right = copy.copy(self.right)
        return result

    def __nonzero__(self):
        return bool(self.data)

    def __cmp__(self, other):
        return cmp(self.key, other.key) if isinstance(other, Node) else cmp(self.key, other)

    def __str__(self):
        return reduce(lambda x, y: x + str(y) + "\n", self.data, "")


class ABB(object):
    def __init__(self):
        self.root = Node()

    def clear(self):
        """Empty the tree"""
        self.root.clear()

    def insert(self, data):
        """Insert a value in tree

        :param data: value to be inserted
        :return: self to allow method chaining
        """
        if not self:
            self.root.append(data)
            return self

        parent, current = self._lookup(data)
        if current:  # data equivalent node found!
            current.append(data)
        else:  # equivalent node not found!
            setattr(parent, "right" if parent < data else "left", Node().append(data))
        return self

    def delete(self, data, wholeNode=False):
        """Deletes the given Node or Value if it is contained, Therefore do nothing

        :type data: Node or ValueType (e.g. User)
        :type wholeNode: bool
        :param data: The node or value to delete
        :param wholeNode: if whole matched node should be deleted or only the matched value
        """
        parent, current = self._lookup(data)
        if current:  # data was found
            current.clearData() if wholeNode else current.delete(data)
            if not current:  # we have deleted the last element from current node!
                if current.left and current.right:  # 2 children
                    newData = current.right.leftmost()
                    current.clearData()
                    current.append(newData)
                    self.delete(newData)
                elif current.left:  # only left child
                    current.data = current.left.data
                    current.right = current.left.right
                    current.left = current.left.left
                    # TODO
                elif current.right:  # only right child
                    current.data = current.right.data
                    current.left = current.right.left
                    current.right = current.right.right
                    # TODO
                else:  # no children
                    if not parent:
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
            if self:
                current = self.root
            else:
                return self  # break

        if current > threshold:
            if current.left:
                self.deleteLower(threshold, current.left, current)
        elif current < threshold:
            if current.right:
                current.data = current.right.data
                current.left = current.right.left
                current.right = current.right.right
                self.deleteLower(threshold, current, parent)
            else:
                if parent:
                    parent.left = None  # restart current
                else:
                    self.clear()  # restart root
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
            if self:
                current = self.root
            else:
                return self  # break

        if current < threshold:
            if current.right:
                self.deleteHigher(threshold, current.right, current)
        elif current > threshold:
            if current.left:
                current.data = current.left.data
                current.right = current.left.right
                current.left = current.left.left
                self.deleteHigher(threshold, current, parent)
            else:
                if parent:
                    parent.right = None  # restart current
                else:
                    self.clear()  # restart root
        else:  # equals
            current.right = None

        return self

    def _lookup(self, data):
        """Internal method. Finds the given value and return the node where it IS or where it SHOULD BE (i.e. None) and
        also his parent node.

        :rtype: Node, Node
        """
        parent, current = None, self.root
        while current:
            if current < data:  # data should be in right
                parent, current = current, current.right
            elif current > data:  # data should be in left
                parent, current = current, current.left
            else:  # equals
                return parent, current
        return parent, current

    @property
    def min(self):
        """Returns the minimum value of the tree"""
        return self.root.leftmost

    @property
    def max(self):
        """Returns the maximum value of the tree"""
        return self.root.rightmost

    @property
    def depth(self):
        return self.root.depth

    def __copy__(self):
        """Returns a copy of self

        :rtype : ABB
        """
        result = ABB()
        result.root = copy.copy(self.root)
        return result

    def __nonzero__(self):
        """Returns false if the tree is empty, therefore returns true"""
        return self.root.__nonzero__()

    def __iter__(self, current=None):
        """Creates a generator that walks through the tree in descending order

        :param current: The current node
        :type current: Node
        """
        if current is None:  # first call
            current = self.root

        if current.right:
            for x in self.__iter__(current.right):
                yield x
        for x in current.data:
            yield x
        if current.left:
            for x in self.__iter__(current.left):
                yield x

    def __str__(self):
        return reduce(lambda x, y: x + str(y) + "\n", self, "")