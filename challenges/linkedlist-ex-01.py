# Given a Singly Linked List, write a function which takes in the first node and returns a boolean indicating if the linked list contains a cycle.

# cycle = when a node in the list points back to a previous node in the list, making a circular linked list 


class Node(object):

    def __init__(self, value):
        self.value = value 
        self.nextnode = None

    def is_circular(self):
        # Have two markers traversing through the linked list
        marker = self
        head_node = marker

        while marker != None:
            marker = marker.nextnode
            if marker == head_node:
                return True


        return False


# create a linked list

a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c

# create a circular linked list 

x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z
z.nextnode = x


#test out the solution

print(a.is_circular())  #False
print(x.is_circular())  #True 
