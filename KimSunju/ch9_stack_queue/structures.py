class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.top=None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top is None:
            return None

        topNode = self.top
        self.top=self.top.next

        return topNode.item

    def is_empty(self):
        return self.top is None


class Queue:
    def __init__(self):
        self.front = None

    def push(self, value):
        if not self.front:
            self.front = Node(value, None)
            return

        node = self.front
        while node and node.next:
            node = node.next
        node.next = Node(value, None)

    def pop(self):
        if not self.front:
            return None

        node = self.front
        self.front = self.front.next
        return node.item

    def is_empty(self):
        return self.front is None