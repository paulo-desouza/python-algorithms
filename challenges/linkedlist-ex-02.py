# Write a function to reverse a linked list in place. The function should take the head of the list and return the new head of the list.

# my solution (works):
# Linear Time complexity!
class Node(object):
    def __init__(self, value):
        self.value = value 
        self.nextnode = None

    def reverser(self):
        traverser = self
        l = []

        while True:
            l.append(traverser)
            traverser = traverser.nextnode
            if traverser.nextnode == None:
                l.append(traverser)
                break
        
        l.reverse()
        
         
        for key, node in enumerate(l):
            
            if key == len(l)-1:
                node.nextnode = None
            else:
                node.nextnode = l[key+1]

        return l[0]

    # lecture solution:
    
    def reverser2(self):

        current = self 
        previous = None
        next = None

        while current != None:

            next = current.nextnode

            current.nextnode = previous

            previous = current 
            current = next

        return previous




a = Node(1)
b = Node(2) 
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

a.reverser() # returns d (new head)

print(d.nextnode.value) #expected 3
print(c.nextnode.value) #expected 2 
print(a.nextnode)

