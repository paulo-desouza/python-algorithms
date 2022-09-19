# Tree Nodes and references implemented.

class BinaryTree(object):

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)

        else:
            # create a new branch if not empty 
            t = BinaryTree(newNode)

            # store the existing leaf/subtree as a child of this new node/branch (push it down one level on the tree)
            t.leftChild = self.leftChild

            # the new subtree now formed, add to the hierarchy.
            self.leftChild = t


    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)

        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootValue(self, obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key

    #traversing examples
    #pre-order as method
    def preorder(self):
        print(self.key)

        if self.leftChild:
            self.leftChild.preorder()

        if self.rightChild:
            self.rightChild.preorder()

#postorder as a function
def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())



r = BinaryTree('/')

r.insertLeft('Downloads')

r.insertLeft('camp')

r.insertLeft('home')

r.insertRight('etc')
print(r.key, r.getLeftChild().getRootVal(), '/', r.getLeftChild().getLeftChild().getRootVal())

r.preorder()
postorder(r)