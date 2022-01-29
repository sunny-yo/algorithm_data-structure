# https://leetcode.com/problems/insertion-sort-list/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = start_node = ListNode(0)

        while head:
            while curr_node.next and curr_node.next.val < head.val:
                curr_node = curr_node.next

            curr_node.next, head.next, head = head, curr_node.next, head.next

            if head and curr_node.val > head.val:
                curr_node = start_node

        return start_node.next

s = Solution()
print(s.insertionSortList(ListNode(4, ListNode(2, ListNode(1, ListNode(3))))))