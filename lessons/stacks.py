# Stacks Queues and Deques

# A stack is an ordered collection of items where the addition/removal of items always takes place at the top.
# The end oposite to the top is known as the base.

# The items close to the base of the stack have been there the longest 
# LAST IN FIRST OUT


class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)




