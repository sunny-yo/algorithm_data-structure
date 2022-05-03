from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        def makeBST(list):
            if not list:
                return

            root = TreeNode()
            root.val = list[len(list) // 2]

            root.left = makeBST(list[:len(list) // 2])
            root.right = makeBST(list[len(list) // 2 + 1:])

            return root

        tree = makeBST(nums)

        return tree


s = Solution()
print(s.sortedArrayToBST([-10, -3, 0, 5, 9]))
