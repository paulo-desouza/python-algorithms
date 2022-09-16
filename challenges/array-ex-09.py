# Implement a Queue using 2 stacks

# Uses lists as stacks 

# a stack is first in first out, queue is first in first out. 

class Queue():
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, item):
        self.instack.append(item)
        

    def dequeue(self):
        
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
                
        return self.outstack.pop()
