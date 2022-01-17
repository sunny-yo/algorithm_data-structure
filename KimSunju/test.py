class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node1 = ListNode(1)
node2 = ListNode(3)
node1.next = node2
head = node1

print(head)