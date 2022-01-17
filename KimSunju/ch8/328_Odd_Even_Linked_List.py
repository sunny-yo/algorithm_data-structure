from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head(input으로 들어온 연결리스트)가 None일 때 None으로 return
        if head is None:
            return None

        # 하나의 연결리스트를 head -> odd, even_head -> even 두개의 연결리스트로 나눈다
        # (이후에 두개를 연결해줌)
        # odd list 뒤에 even list를 연결해야하기 때문에 even의 시작점을 even_head에 할당한다
        odd = head
        even = head.next
        even_head = even

        # even과 even.next가 None일 경우 while문을 종료한다
        # while문을 돌고 오면 even과 even.next는 같은 값을 가리킨다
        while even and even.next:
            # odd.next는 노드를 2번 건너뛰어 다음 홀수번째 노드를 가리킨다
            # even.next는 노드를 2번 건너뛰어 다음 짝수번째 노드를 가리킨다
            odd.next = odd.next.next
            even.next = even.next.next
            # odd와 even이 odd.next와 even.next가 가리키는 곳을 가리킨다
            odd = odd.next
            even = even.next

        # odd.next가 even_head를 가리키게 되면 odd의 list와 even의 list가 이어진다
        odd.next = even_head

        # 연결리스트 순서대로 print해서 확인하기 위한 코드
        # while head:
        #     print(head.val)
        #     head = head.next

        return head

s = Solution()
print(s.oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))))