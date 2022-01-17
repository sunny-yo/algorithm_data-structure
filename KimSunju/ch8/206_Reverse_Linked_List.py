from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        b_head = head
        prev = None

        while b_head:
            next, b_head.next = b_head.next, prev
            prev, b_head = b_head, next

        return prev

# b_head가 head로 들어온 연결리스트를 한칸씩 이동하면서
# 그 값을 prev라는 새로운 연결리스트의 앞으로 연결한다

s = Solution()
print(s.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))))