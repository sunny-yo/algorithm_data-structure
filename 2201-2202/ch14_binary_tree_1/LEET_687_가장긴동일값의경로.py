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
    def longestUnivaluePath(self, lst) -> int:
        root = make_tree_by(lst, 0)

        def dfs(root):
            nonlocal max_length
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            if root.left and root.left.val == root.val:
                left += 1
            else:
                left = 0
            if root.right and root.right.val == root.val:
                right += 1
            else:
                right = 0

            max_length = max(max_length, left + right)
            return max(left, right)

        max_length = 0
        dfs(root)

        return max_length


s = Solution()
print(s.longestUnivaluePath([5, 4, 5, 1, 1, None, 5]))
print(s.longestUnivaluePath([1, 4, 5, 4, 4, 5, None]))


''' 첫번째 풀이
틀린 이유 : 서브트리의 루트와 자식노드의 값이 같을 경우를 구상하지 않음
class Solution:
    def longestUnivaluePath(self, lst) -> int:
        root = make_tree_by(lst, 0)

        def dfs(root, curr_val, length):
            nonlocal max_length
            max_length = max(max_length, length)
            if not root:
                return

            if root.left and root.left.val == curr_val:
                dfs(root.left, root.left.val, length + 1)
            elif root.left and root.left.val != curr_val:
                dfs(root.left, root.left.val, 0)
            else:
                dfs(root.left, None, 0)

            if root.right and root.right.val == curr_val:
                dfs(root.right, root.right.val, length + 1)
            elif root.right and root.right.val != curr_val:
                dfs(root.right, root.right.val, 0)
            else:
                dfs(root.right, None, 0)

        max_length = 0
        dfs(root, root.val, 0)

        return max_length
'''