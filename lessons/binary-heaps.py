# Priority Queues with Binary Heaps

# acts like a queue in that you dequeue from the front,
# but the logical order of items inside a queue is DETERMINED BY their PRIORITY

# a NEW ITEM may move all the way to the front based on its priority!

# a classic way to implement a priority queue is using a data structure 
# called a BINARY HEAP. It allows us to both enqueue and dequeue items in O(logn).

# It has two common variations: the min heap in which the smallest key is always at the front,
# and the max heap, in which the largest key is always at the front. 
# 
#  MIN HEAP IMPLEMENTATION:

class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    # when inserting an element to the tree, we will append it to the end of the list, and check to see if its bigger than the parent. 
    # We will then swap the new element with the parent if need be, and repeat this process.

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_ist[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def send_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[1 // 2]:
                temp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = temp
            i = i // 2

    def send_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = temp
            i = mc

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.send_up(self.current_size)

    def delete_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.send_down(1)
        return retval