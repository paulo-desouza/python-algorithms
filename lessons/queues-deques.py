# Queues
# Ordered collection of items where the new items are added to the rear, and removal of items happens at the front. 
# FIRST IN FIRST OUT
# Enqueue: adding an item
# Dequeue: removing an item
 
class Queue():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# Deque
# Items can be added either to the front or the rear.
# Can also be removed from either end.

class Deque():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    
    



