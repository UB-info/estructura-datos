class Node:
    __slots__ = ('data', 'left', 'right')

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print str(self.data),
        if self.right is not None:
            self.right.inorder()

    def swap(self):
        if self.left is not None and self.right is not None:#have 2 childs
            self.left.data, self.right.data = self.right.data, self.left.data
        if self.left is not None:
            self.left.swap()
        if self.right is not None:
            self.right.swap()

    def depth(self):
        d = []
        if self.right is None and self.left is None:
            return [0]
        
        if self.left is not None:
            for x in self.left.depth():
                d.append(x + 1)
        else:
            d.append(0)
        if self.right is not None:
            for x in self.right.depth():
                d.append(x + 1)
        else:
            d.append(0)

        #print self.data, d#debug
        return d

class ABB:
    __slots__ = ('root')
    
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def add(self, data):
        n = Node(data)

        if self.isEmpty():
            self.root = n
        else:
            r, br = self.root, None
            while r != None:
                if n.data > r.data:#must be right child
                    r, br = r.right, r
                elif n.data < r.data:#must be left child
                    r, br = r.left, r
                else:#equals
                    return None

            if n.data > br.data:
                br.right = n
            else:
                br.left = n

    def inorder(self):
        self.root.inorder()
        print "\n"

    def swap(self):
        self.root.swap()

    def depth(self):
        return self.root.depth()

    def __str__(self):
        out = ""
        floor = []
        floor.append(self.root)
        nextFloor = True
        while nextFloor:
            nextFloor = False
            out += reduce(lambda x, y: x + (". " if y == None else str(y.data) + " "), floor, "") + "\n"
            floor, oldfloor = [], floor
            for n in oldfloor:
                if n == None:
                    floor.append(None)
                    floor.append(None)
                else:
                    if n.left != None or n.right != None:
                        nextFloor = True
                        
                    floor.append(n.left)
                    floor.append(n.right)
    
        return out

if __name__ == '__main__':#debug
    arbol = ABB()
    arbol.add(8)
    arbol.add(4)
    arbol.add(12)
    arbol.add(2)
    arbol.add(6)
    arbol.add(10)
    arbol.add(14)
    arbol.add(3)
    arbol.add(5)
    arbol.add(11)
    arbol.add(15)

    print arbol

    arbol.inorder()
    arbol.swap()
    print arbol
    arbol.inorder()
    print arbol.depth()

#arbol.inorder()



