# https://leetcode.com/problems/sort-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        lst = []
        while p:
            lst.append(p.val)
            p = p.next

        lst.sort()

        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head

s = Solution()
print(s.sortList(ListNode(4, ListNode(2, ListNode(1, ListNode(3))))))

'''
# 퀵 소트로 구현 : time limit exceeded
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def quick_sort(node):
            if node is None:
                return [None, None]
            if node and node.next is None:
                return [node, node]

            def partition(root):
                lo = lo_start = ListNode(None)

                pivot = root
                prev_pointer = root
                pointer = root.next

                while pointer:
                    if pivot.val <= pointer.val:
                        prev_pointer = pointer
                        pointer = pointer.next
                    else:
                        lo.next, pointer, prev_pointer.next = pointer, pointer.next, pointer.next
                        lo, lo.next = lo.next, None
                return [lo_start.next, pivot, pivot.next]

            [first, pivot, last] = partition(node)
            [f_start, f_end] = quick_sort(first)
            [l_start, l_end] = quick_sort(last)

            if first and last:
                f_end.next = pivot
                pivot.next = l_start
                return [f_start, l_end]
            elif first and last is None:
                f_end.next = pivot
                return [f_start, pivot]
            elif last and first is None:
                pivot.next = l_start
                return [pivot, l_end]

        answer = quick_sort(head)[0]
        print(answer.val, answer.next.val, answer.next.next.val, answer.next.next.next.val)
        return answer
'''
