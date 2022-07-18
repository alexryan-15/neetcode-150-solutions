# There are three solutions to solving this problem that are all valid. The first, and easiest, is a recursive
# DFS approach which adds one to every iteration. The second, is a iterative DFS approach which uses a stack.
# The third approach uses BFS where we track the level of the tree.

# RECURSIVE DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# ITERATIVE DFS   
class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [[root, 1]]
        res = 0
        
        while stack:
            node, depth = stack.pop()
        
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

# BFS
from collections import deque
class Solution3:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        while q:
            
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level