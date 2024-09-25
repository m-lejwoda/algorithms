class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [[root,1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res,depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return res
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
s = Solution()
print(s.maxDepth(root))