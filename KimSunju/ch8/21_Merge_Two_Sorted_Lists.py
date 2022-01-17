from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2

        if not l1:
            return list2
        elif not l2:
            return list1

        result = list2 if l1.val>l2.val else list1

        while l1.val and l2.val:
            if l1.val > l2.val:
                while l1.val > l2.next.val:
                    if l2.next.next is None:
                        l2 = l2.next
                        break
                    else: l2 = l2.next
                l2.next, l2 = l1, l2.next
            else:
                while not l1 and l2.val > l1.next.val:
                    if l1.next.next is None:
                        l1 = l1.next
                        break
                    else: l1 = l1.next
                l1.next, l1 = l2, l1.next

            if l1 is None or l2 is None:
                break
        return result


s = Solution()
print(s.mergeTwoLists((ListNode(2, ListNode(4, ListNode(5, None)))), ListNode(1, ListNode(2, ListNode(4, None)))))
