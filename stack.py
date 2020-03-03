from collections import deque


class Stack(object):
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        # no argument specified for popping(complexity is O(1))
        return self.items.pop()

    def size(self):
        return len(self.items)
