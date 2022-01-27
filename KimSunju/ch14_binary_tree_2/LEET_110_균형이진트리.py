class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree_by(lst, idx):
    parent = None
    if idx < len(lst):
        value = lst[idx]
        if value == None:
            return

        parent = TreeNode(value)
        parent.left = make_tree_by(lst, 2 * idx + 1)
        parent.right = make_tree_by(lst, 2 * idx + 2)

    return parent


class Solution:
    def isBalanced(self, lst):
        root = make_tree_by(lst, 0)

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return dfs(root) != -1

s = Solution()
print(s.isBalanced([3, 9, 20, None, None, 15, 7]))
print(s.isBalanced([1, 2, 2, 3, 3, None, None, 4, 4]))
