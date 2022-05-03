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
    def invertTree(self, lst):
        root = make_tree_by(lst, 0)

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            dfs(root.right)
            root.left, root.right = root.right, root.left

        dfs(root)

        return root


s = Solution()
print(s.invertTree([4, 2, 7, 1, 3, 6, 9]))
