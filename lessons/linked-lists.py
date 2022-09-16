# Singly Linked Lists

# Beginnings are called heads, and ends are called tails. Traversing means hopping from node to node on the linked list. 
# We can insert elements either to the end head or tail of the linked list, not forgetting to updte the "tail" or "head" reference afterwards.


class Node(object):

    def __init__(self, value):

        self.value = value
        self.nextnode = None


a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c


# Doubly Linked Lists 

# Each node has a reference to both the nodes after it and before it.
# continue using term "next" to reference the node after it, and use the term "previous" to reference the node before.

# header and trailer instead of head and tail

# how to traverse through a linked list?
# have a checker referencing the first node, and have it receive checker.nextnode inside a loop, where the loop's flag is nextnode == None

class DoublyNode(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None
        self.prevnode = None


A = DoublyNode(1)
B = DoublyNode(2)
C = DoublyNode(3)

A.nextnode = B
B.prevnode = A

B.nextnode = C
C.prevnode = B

