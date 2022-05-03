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
    def diameterOfBinaryTree(self, lst):
        root = make_tree_by(lst, 0)

        def dfs(root):
            nonlocal diameter
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1

        diameter = 0
        dfs(root)

        return diameter


s = Solution()
print(s.diameterOfBinaryTree([1, 2, 3, 4, 5, None, None]))
print(s.diameterOfBinaryTree([1, 2, None]))
print(s.diameterOfBinaryTree(
    [4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None, None, -1, -4,
     None, None, None, -2]))

''' 첫번째 풀이
# 틀린 이유 : 최대 직경이 꼭 root를 지나가야하는 것은 아니다
class Solution:
    def diameterOfBinaryTree(self, lst):
        root = make_tree_by(lst, 0)
        if not root:
            return 0

        def bfs(q, depth):
            while q:
                depth += 1
                for _ in range(len(q)):
                    curr = q.popleft()
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            return depth

        if root.left:
            q1 = deque([root.left])
            d1 = bfs(q1, 0)
        else:
            d1 = 0
        if root.right:
            q2 = deque([root.right])
            d2 = bfs(q2, 0)
        else:
            d2 = 0

        return d1 + d2
'''
