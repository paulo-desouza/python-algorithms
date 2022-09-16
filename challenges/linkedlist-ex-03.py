# Singly Linked List Nth to last node

# Write a function that takes a head node and an integer value N, and then returns the Nth to last node in the linked list.
# personal note: a doubly linked list would be very much useful here.
from email import header


class Node(object):

    def __init__(self, value):

        self.value = value
        self.nextnode = None


# my solution, linear time complexity:

    def node_locator(self, n):
        tracker1 = self
        tracker2 = self
        link_length = 0

        while tracker1 != None:
            tracker1 = tracker1.nextnode
            link_length += 1

        for c in range(link_length - n):
            tracker2 = tracker2.nextnode
        
        return tracker2
            
# lecture solution:

    def node_locator2(self, n):
        left_pointer = self
        right_pointer = self

        # Edge Case:
        for i in range(n-1):

            if not right_pointer.nextnode:
                raise LookupError('Error: n is larger than the linked list!')
            
            right_pointer = right_pointer.nextnode

        while right_pointer.nextnode:

            left_pointer = left_pointer.nextnode
            right_pointer = right_pointer.nextnode

        return left_pointer




a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

print(a.node_locator(1).value)