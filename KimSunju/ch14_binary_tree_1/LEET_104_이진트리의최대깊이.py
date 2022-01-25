from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        tree_list = deque(root)
        q = deque([tree_list.popleft()])
        depth = 0

        while q:
            depth += 1
            if not tree_list:
                break
            for _ in range(2**(depth-1)):
                q.popleft()
            for _ in range(2**depth):
                q.append(tree_list.popleft())

        return depth


s = Solution()
print(s.maxDepth([3, 9, 20, None, None, 15, 7]))

'''
# 리트코드 제출
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        q = deque([root])
        depth = 0

        while q:
            depth += 1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return depth
'''
