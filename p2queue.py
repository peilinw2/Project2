"""
Math 560
Project 2
Fall 2021

p2queue.py

Partner 1: Amy Wang
Partner 2: Lu Liu
Date: 11/02/2021
"""

"""
Queue Class
"""
class Queue:

    """
    Class attributes:
    queue    # The array for the queue.
    front    # The index of the front of the queue.
    rear     # The index ONE PAST the rear of the queue.
    numElems # The number of elements in the queue.
    """

    """
    __init__ function to initialize the Queue.
    Note: initially the size of the queue defaults to 3.
    Note: the queue is initially filled with None values.
    """
    def __init__(self, size=3):
        self.queue = [None for x in range(0,size)]
        self.front = 0
        self.rear = 0
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.queue)) + ' ]\n'
        s += ('Front: %d' % self.front) + '\n'
        s += ('Rear: %d' % self.rear) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the queue is full.
    """
    def isFull(self):
        if self.numElems == len(self.queue):
            return True
        return False


    """
    isEmpty function to check if the queue is empty.
    """
    def isEmpty(self):
        if self.numElems == 0:
            return True
        return False

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    Input:queue
    Output:queue with the resized array
    """
    def resize(self):
        # Reset the front to index 0
        if self.rear <= self.front:
            self.queue = self.queue[self.front:] + self.queue[self.rear:]
        self.front = 0
        self.rear = self.numElems
        #Resize the queue by doubling its size
        self.queue = self.queue + [None for x in self.queue]
        return

    """
    push function to push a value into the rear of the queue.
    Input:queue and new value 
    Ouput:queue with the value being pushed
    """
    def push(self, val):
        #We first check if the queue is full, and we will resize if it is full
        if self.isFull() is True:
            self.resize()
        #Wrap around the queue
        self.queue[self.rear] = val
        self.rear = (self.rear +1) % len(self.queue)
        self.numElems = self.numElems + 1
        return

    """
    pop function to pop the value from the front of the queue.
    Input: queue
    Output: queue with the front element being removed
    """
    def pop(self):
        #We first check if the queue is empty, and we will exit if the queue is empty
        if self.isEmpty() is True:
            return None
        #Wrap around the queue
        temp = self.queue[self.front]
        self.front = (self.front +1) % len(self.queue)
        self.numElems = self.numElems -1
        return temp


